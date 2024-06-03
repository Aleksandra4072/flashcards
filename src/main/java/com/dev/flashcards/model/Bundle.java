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
@Table(name = "bundles")
public class Bundle {
    @Id
    @Column(name = "id", nullable = false, unique = true)
    @Schema(description = "Bundle ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Column(name = "title", nullable = false)
    @Schema(description = "Bundle tittle", example = "Some bundle title")
    private String title;

    @Column(name = "description")
    @Schema(description = "Bundle description", example = "Some bundle description")
    private String description;

    @Column(name = "subject")
    @Schema(description = "Bundle subject", example = "Some bundle subject")
    private String subject;

    @Column(name = "user_id", nullable = false)
    @Schema(description = "Bundle Author ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String user_id;
}
