package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "users")
public class User {
    @Id
    @Column(name = "id", nullable = false, unique = true)
    @Schema(description = "User ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Column(name = "username",nullable = false)
    @Schema(description = "Username of the user", example = "john_doe")
    private String username;

    @Column(name = "email", nullable = false, unique = true)
    @Schema(description = "Email address of the user", example = "john@example.com")
    private String email;

}
