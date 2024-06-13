package com.dev.flashcards.controller;

import com.dev.flashcards.config.security.JwtAuthenticationFilter;
import com.dev.flashcards.dto.LoginUserDto;
import com.dev.flashcards.dto.RegisterUserDto;
import com.dev.flashcards.model.User;
import com.dev.flashcards.responses.LoginResponse;
import com.dev.flashcards.service.AuthService;
import com.dev.flashcards.service.JwtService;
import io.swagger.v3.oas.annotations.security.SecurityRequirements;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
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

    @Autowired
    private JwtAuthenticationFilter jwtFilter;

    public AuthController(
            JwtService jwtService,
            AuthService authService
    ) {
        this.authService = authService;
        this.jwtService = jwtService;
    }

    @PostMapping("/signup")
    public ResponseEntity<String> register(@RequestBody RegisterUserDto registerUserDto) {
        authService.signup(registerUserDto);

        return ResponseEntity.ok("User registered");
    }

    @PostMapping("/login")
    public ResponseEntity<LoginResponse> authenticate(@RequestBody LoginUserDto loginUserDto) {
        User authenticatedUser = authService.authenticate(loginUserDto);

        String jwtToken = jwtService.generateAccessToken(authenticatedUser);

        LoginResponse loginResponse = new LoginResponse();
        loginResponse.setToken(jwtToken);

        jwtFilter.getUserDetails(jwtToken);

        return ResponseEntity.ok(loginResponse);
    }
}
