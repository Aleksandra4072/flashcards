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
@Table(name = "cards")
public class Card {
    @Id
    @Column(name = "id", nullable = false, unique = true)
    @Schema(description = "Card ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Column(name = "term", nullable = false)
    @Schema(description = "Card term", example = "Some card term")
    private String term;

    @Column(name = "definition")
    @Schema(description = "Card definition", example = "Some card definition")
    private String definition;

    @Column(name = "img")
    @Schema(description = "Card image url", example = "Some card image url")
    private String img;

    @Column(name = "bundle_id", nullable = false)
    @Schema(description = "Card Bundle ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String bundle_id;
}

