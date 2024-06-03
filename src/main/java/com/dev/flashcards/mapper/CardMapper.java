package com.dev.flashcards.mapper;

import com.dev.flashcards.model.Card;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.UUID;

@Mapper
public interface CardMapper {
    @Select("SELECT * FROM cards")
    List<Card> findALl();

    @Select("SELECT * FROM cards WHERE bundle_id = #{id}")
    List<Card> findById(@Param("id") UUID id);

    @Select("DELETE FROM cards WHERE bundle_id = #{bundleId}")
    void deleteByBundleId(@Param("bundleId") UUID bundleId);

    @Select("DELETE FROM cards WHERE id = #{id}")
    void deleteById(@Param("id") UUID id);
}
