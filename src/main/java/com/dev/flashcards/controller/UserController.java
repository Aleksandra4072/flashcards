package com.dev.flashcards.controller;

import com.dev.flashcards.mapper.UserMapper;
import com.dev.flashcards.model.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/user")
public class UserController {

    private final UserMapper userMapper;

    public UserController(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    @GetMapping("")
    public List<User> getAll() {
        return userMapper.findALl();
    }
}
