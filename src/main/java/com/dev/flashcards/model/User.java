package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Collection;
import java.util.Date;
import java.util.List;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "users")
public class User implements UserDetails {
    @Id
    @Column(name = "id", nullable = false, unique = true)
    @Schema(description = "User ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Column(name = "email", nullable = false, unique = true)
    @Schema(description = "Email address of the user", example = "john@example.com")
    private String email;

    @Column(nullable = false, name = "password")
    @Schema(description = "Password of a user", example = "!StrongPassword123!")
    private String password;

    @Column(updatable = false, name = "created_at", nullable = false)
    @Schema(description = "Date fo creation", example = "2024-06-11")
    private Date createdAt;

    @Column(name = "updated_at")
    @Schema(description = "Date of update", example = "2024-06-11")
    private Date updatedAt;

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of();
    }

    @Override
    public String getUsername() {
        return email;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
