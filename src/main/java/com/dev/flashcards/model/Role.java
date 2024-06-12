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
@Table(name = "roles")
public class Role {
    @Id
    @Column(name = "id", nullable = false, unique = true)
    @Schema(description = "Role ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Column(name = "name", nullable = false, unique = true)
    @Schema(description = "Role name", example = "ADMIN")
    private String name;

    @Column(name = "description")
    @Schema(description = "Role descriptions", example = "Some role descriptions")
    private String description;
}
