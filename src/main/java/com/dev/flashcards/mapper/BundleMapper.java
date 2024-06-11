package com.dev.flashcards.mapper;

import com.dev.flashcards.model.Bundle;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;
import java.util.UUID;

@Mapper
public interface BundleMapper {
    @Select("SELECT * FROM bundles WHERE user_id = #{userId}")
    List<Bundle> findALlByUserID(@Param("userId") UUID userId);

    @Select("SELECT * FROM bundles WHERE id = #{id}")
    Bundle findById(@Param("id") UUID id);

    @Select("DELETE FROM bundles WHERE user_id = #{userId}")
    void deleteByUserId(@Param("userId") UUID userId);

    @Delete("DELETE FROM bundles WHERE id = #{id}")
    void deleteById(@Param("id") UUID id);

    @Insert("INSERT INTO bundles " +
            "(title, description, subject, user_id) " +
            "VALUES (#{title}, #{description}, #{subject}, #{user_id})")
    void addBundle(Bundle bundle);

    @Update("UPDATE users " +
            "SET title=#{title}, description=#{description}, subject=#{subject}" +
            " WHERE id=#{id}")
    void updateBundle(@Param("id") UUID id, Bundle bundle);
}
