package com.dev.flashcards.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.time.Instant;
import java.util.UUID;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class RefreshToken {

    @Schema(description = "Refresh token ID", example = "123e4567-e89b-12d3-a456-556642440000")
    private UUID id;

    @Schema(description = "Token", example = "123e4567-e89b-12d3-a456-556642440000")
    private String token;

    @Schema(description = "Expiration date", example = "2024-06-23 08:02:55.559826 +00:00")
    private Instant expiry_date;

    @Schema(description = "User Id")
    private UUID user_id;
}
