package com.dev.flashcards.mapper;

import com.dev.flashcards.model.Bundle;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.UUID;

@Mapper
public interface BundleMapper {
    @Select("SELECT * FROM bundles")
    List<Bundle> findALl();

    @Select("SELECT * FROM bundles WHERE user_id = #{userId}")
    List<Bundle> findByUserId(@Param("userId") UUID userId);

    @Select("DELETE FROM bundles WHERE user_id = #{userId}")
    void deleteByUserId(@Param("userId") UUID userId);

    @Delete("DELETE FROM bundles WHERE id = #{id}")
    void deleteById(@Param("id") UUID id);
}
