package com.dev.flashcards.service;

import com.dev.flashcards.mapper.RefreshTokenMapper;
import com.dev.flashcards.mapper.UserMapper;
import com.dev.flashcards.model.RefreshToken;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.Optional;
import java.util.UUID;

@Slf4j
@Service
public class RefreshTokenService {
    private final RefreshTokenMapper refreshTokenMapper;
    private final UserMapper userMapper;

    private RefreshTokenService (
        RefreshTokenMapper refreshTokenMapper,
        UserMapper userMapper
    ) {
        this.refreshTokenMapper = refreshTokenMapper;
        this.userMapper = userMapper;
    }

    public RefreshToken createRefreshToken(String username){
        RefreshToken refreshToken = RefreshToken.builder()
                .user_id(userMapper.findByEmail(username).getId())
                .token(UUID.randomUUID().toString())
                .expiry_date(Instant.now().plus(7, ChronoUnit.DAYS)) // set expiry of refresh token to 10 minutes - you can configure it application.properties file
                .build();
        refreshTokenMapper.add(refreshToken);
        return refreshToken;
    }

    public Optional<RefreshToken> findByToken(String token){
        return refreshTokenMapper.findByToken(token);
    }

    public RefreshToken verifyExpiration(RefreshToken token){
        log.info("Checking the expiration date of the refresh token: " + token);

        if(token.getExpiry_date().isBefore(Instant.now())){
            refreshTokenMapper.delete(token.getId());
            throw new RuntimeException("Refresh token is expired. Please make a new login..!");
        }

        return token;
    }
}
