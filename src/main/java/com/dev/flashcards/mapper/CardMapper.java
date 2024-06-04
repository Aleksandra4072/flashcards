package com.dev.flashcards.mapper;

import com.dev.flashcards.model.Card;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.UUID;

@Mapper
public interface CardMapper {
    @Select("SELECT * FROM cards WHERE bundle_id=#{bundleId}")
    List<Card> findALlByBundleId(@Param("bundleId") UUID bundleId);

    @Select("SELECT * FROM cards WHERE id=#{id}")
    Card findById(@Param("id") UUID id);

    @Delete("DELETE FROM cards WHERE bundle_id = #{bundleId}")
    void deleteByBundleId(@Param("bundleId") UUID bundleId);

    @Delete("DELETE FROM cards WHERE id = #{id}")
    void delete(@Param("id") UUID id);
}
