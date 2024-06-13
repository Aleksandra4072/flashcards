package com.dev.flashcards.controller;

import com.dev.flashcards.dto.UserDto;
import com.dev.flashcards.model.User;
import com.dev.flashcards.service.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.UUID;

@SecurityRequirement(name = "bearerAuth")
@Tag(name = "Users")
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @Operation(summary = "Get all the users", description = "Returns a list of users")
    @GetMapping("")
    public List<UserDto> getAll() {
        return userService.getAll();
    }

    @Operation(summary = "Get user by ID", description = "Returns a user")
    @GetMapping("/{id}")
    public User getUserById(@PathVariable String id) {
        UUID uuid = UUID.fromString(id);
        return userService.getById(uuid);
    }

    @Operation(summary = "Delete user by ID", description = "Returns void")
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable String id) {
        UUID uuid = UUID.fromString(id);
        userService.delete(uuid);
    }

    @Operation(summary = "Create user", description = "Create user")
    @PostMapping("")
    public void createUser(@RequestBody User user) {
        userService.createUser(user);
    }

    @Operation(summary = "Update user", description = "Update user")
    @PutMapping("/{id}")
    public void updateUser(@PathVariable String id, @RequestBody User user) {
        UUID uuid = UUID.fromString(id);
        userService.updateUser(uuid, user);
    }
}
