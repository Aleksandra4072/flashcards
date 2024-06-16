package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Bundle {

    @Schema(description = "Bundle ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private UUID id;

    @Schema(description = "Bundle tittle", example = "Some bundle title")
    private String title;

    @Schema(description = "Bundle description", example = "Some bundle description")
    private String description;

    @Schema(description = "Bundle subject", example = "Some bundle subject")
    private String subject;

    @Schema(description = "Bundle Author ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private UUID user_id;
}
