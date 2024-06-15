package com.dev.flashcards.mapper;

import com.dev.flashcards.model.RefreshToken;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.Optional;

@Mapper
public interface RefreshTokenMapper {

    @Select("SELECT * FROM refresh_tokens WHERE token = #{token}")
    Optional<RefreshToken> findByToken(@Param("token") String token);

}
