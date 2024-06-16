package com.dev.flashcards.mapper;

import com.dev.flashcards.model.RefreshToken;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.Optional;
import java.util.UUID;

@Mapper
public interface RefreshTokenMapper {

    @Select("SELECT * FROM refresh_tokens WHERE token = #{token}")
    Optional<RefreshToken> findByToken(@Param("token") String token);

    @Select("SELECT * FROM refresh_tokens WHERE user_id = #{userId}")
    RefreshToken findByUserId(@Param("userId") UUID userId);

    @Insert("INSERT INTO refresh_tokens(token, expiry_date, user_id) VALUES (#{token}, #{expiry_date}, #{user_id})")
    void add(RefreshToken refreshToken);

    @Insert("DELETE FROM refresh_tokens WHERE id=#{id}")
    void delete(@Param("id") UUID id);
}
