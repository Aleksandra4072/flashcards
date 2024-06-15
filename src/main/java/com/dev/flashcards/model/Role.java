package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Role {

    @Schema(description = "Role ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Schema(description = "Role name", example = "ADMIN")
    private String name;

    @Schema(description = "Role descriptions", example = "Some role descriptions")
    private String description;

    @Override
    public String toString() {
        return this.name;
    }

    public Role(String name) {
        this.name = name;
    }
}
