package com.dev.flashcards.mapper;

import com.dev.flashcards.model.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import java.util.List;
import java.util.UUID;

@Mapper
public interface UserMapper {
    @Select("SELECT * FROM users")
    List<User> findALl();

    @Select("SELECT * FROM users WHERE id = #{id}")
    User findById(@Param("id") UUID id);

    @Delete("DELETE FROM users WHERE id = #{id}")
    void delete(@Param("id") UUID id);
}
