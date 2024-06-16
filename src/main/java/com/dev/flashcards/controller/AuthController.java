package com.dev.flashcards.controller;

import com.dev.flashcards.config.security.JwtAuthenticationFilter;
import com.dev.flashcards.dto.requests.LoginUserDto;
import com.dev.flashcards.dto.requests.RefreshTokenDto;
import com.dev.flashcards.dto.requests.RegisterUserDto;
import com.dev.flashcards.model.RefreshToken;
import com.dev.flashcards.model.User;
import com.dev.flashcards.dto.responses.LoginResponse;
import com.dev.flashcards.service.AuthService;
import com.dev.flashcards.service.JwtService;
import com.dev.flashcards.service.RefreshTokenService;
import com.dev.flashcards.service.UserService;
import io.swagger.v3.oas.annotations.security.SecurityRequirements;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SecurityRequirements()
@RequestMapping("/auth")
@RestController
public class AuthController {
    private final JwtService jwtService;
    private final AuthService authService;
    private final RefreshTokenService refreshTokenService;
    private final JwtAuthenticationFilter jwtFilter;
    private final UserService userService;

    public AuthController(
            JwtService jwtService,
            AuthService authService,
            RefreshTokenService refreshTokenService,
            JwtAuthenticationFilter jwtFilter,
            UserService userService
    ) {
        this.authService = authService;
        this.jwtService = jwtService;
        this.refreshTokenService = refreshTokenService;
        this.jwtFilter = jwtFilter;
        this.userService = userService;
    }

    @PostMapping("/signup")
    public ResponseEntity<String> register(@RequestBody RegisterUserDto registerUserDto) {
        authService.signup(registerUserDto);

        return ResponseEntity.ok("User registered");
    }

    @PostMapping("/login")
    public ResponseEntity<LoginResponse> authenticate(@RequestBody LoginUserDto loginUserDto) {
        User authenticatedUser = authService.authenticate(loginUserDto);

        if(authenticatedUser.isAccountNonLocked() && authenticatedUser.isAccountNonExpired()) {
            RefreshToken refreshToken = refreshTokenService.createRefreshToken(authenticatedUser.getEmail());

            String accessToken = jwtService.generateAccessToken(authenticatedUser);

            LoginResponse loginResponse = new LoginResponse();
            loginResponse.setAccessToken(accessToken);
            loginResponse.setRefreshToken(refreshToken.getToken());

            jwtFilter.getUserDetails(accessToken);

            return ResponseEntity.ok(loginResponse);
        } else {
            throw new UsernameNotFoundException("invalid user request..!!");
        }
    }

    @PostMapping("/refreshToken")
    public LoginResponse refreshToken(@RequestBody RefreshTokenDto refreshTokenDto){
        return refreshTokenService.findByToken(refreshTokenDto.getRefreshToken())
                .map(refreshTokenService::verifyExpiration)
                .map(refreshToken -> {
                    User user = userService.getById(refreshToken.getUser_id());
                    if (user == null) {
                        throw new RuntimeException("User not found for the refresh token. Please make a new login.");
                    }

                    String accessToken = jwtService.generateAccessToken(user);

                    LoginResponse loginResponse = new LoginResponse();
                    loginResponse.setAccessToken(accessToken);
                    loginResponse.setRefreshToken(refreshTokenDto.getRefreshToken());

                    return loginResponse;
                })
                .orElseThrow(() -> new RuntimeException("Refresh Token is not valid or expired..!!"));
    }
}
