package com.dev.flashcards.service;

import com.dev.flashcards.util.UuidParser;
import com.dev.flashcards.dto.LoginUserDto;
import com.dev.flashcards.dto.RegisterUserDto;
import com.dev.flashcards.mapper.RoleMapper;
import com.dev.flashcards.mapper.UserMapper;
import com.dev.flashcards.model.Role;
import com.dev.flashcards.model.User;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Date;
import java.util.HashSet;

@Slf4j
@Service
public class AuthService {
    private final RoleMapper roleMapper;
    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authManager;


    public AuthService(
            RoleMapper roleMapper,
            UserMapper userMapper,
            PasswordEncoder passwordEncoder,
            AuthenticationManager authManager
    ) {
        this.roleMapper = roleMapper;
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
        this.authManager = authManager;
    }

    @Transactional
    public void signup(RegisterUserDto input) {
        User user = new User();
        if (user.getRoles() == null) {
            user.setRoles(new HashSet<>());
        }

        user.setCreatedAt(new Date());
        user.setEmail(input.getEmail());
        user.setPassword(passwordEncoder.encode(input.getPassword()));

        userMapper.addUser(user);

        User createdUser = userMapper.findByEmail(input.getEmail());
        log.info("Created user: {}", createdUser.getId());
        if(input.getRoleId() == null) {
            Role role = roleMapper.findByName("ROLE_USER");
            roleMapper.addRoleToUser(UuidParser.parse(createdUser.getId()), UuidParser.parse(role.getId()));
        } else {
            Role role = roleMapper.findById(UuidParser.parse(input.getRoleId()));
            roleMapper.addRoleToUser(UuidParser.parse(createdUser.getId()), UuidParser.parse(role.getId()));
        }
    }

    public User authenticate(LoginUserDto input) {
        authManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        input.getEmail(),
                        input.getPassword()
                )
        );

        return userMapper.findByEmail(input.getEmail());
    }

}
