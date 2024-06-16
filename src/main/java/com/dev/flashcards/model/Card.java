package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Card {

    @Schema(description = "Card ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private UUID id;

    @Schema(description = "Card term", example = "Some card term")
    private String term;


    @Schema(description = "Card definition", example = "Some card definition")
    private String definition;

    @Schema(description = "Card image url", example = "Some card image url")
    private String img;

    @Schema(description = "Card Bundle ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private UUID bundle_id;
}

