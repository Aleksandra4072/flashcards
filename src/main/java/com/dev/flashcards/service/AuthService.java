package com.dev.flashcards.service;

import com.dev.flashcards.dto.LoginUserDto;
import com.dev.flashcards.dto.RegisterUserDto;
import com.dev.flashcards.mapper.UserMapper;
import com.dev.flashcards.model.User;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AuthService {
    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authManager;

    public AuthService(
            UserMapper userMapper,
            PasswordEncoder passwordEncoder,
            AuthenticationManager authManager
    ) {
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
        this.authManager = authManager;
    }

    public void signup(RegisterUserDto input) {
        User user = new User();
        user.setEmail(input.getEmail());
        user.setPassword(passwordEncoder.encode(input.getPassword()));

        userMapper.addUser(user);
    }

    public User authenticate(LoginUserDto input) {
        authManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        input.getEmail(),
                        input.getPassword()
                )
        );

        return userMapper.findByEmail(input.getEmail())
                .orElseThrow();
    }

}
