package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.time.Instant;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class RefreshToken {

    @Schema(description = "Refresh token ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private String id;

    @Schema(description = "Token", example = "token")
    private String token;

    @Schema(description = "Token", example = "token")
    private Instant expiryDate;

    @Schema(description = "Token", example = "token")
    private String user_id;
}
