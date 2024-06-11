package com.dev.flashcards.mapper;

import com.dev.flashcards.model.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Mapper
public interface UserMapper {

    @Select("SELECT * FROM users WHERE email = #{email}")
    Optional<User> findByEmail(@Param("email") String email);

    @Select("SELECT * FROM users")
    List<User> findALl();

    @Select("SELECT * FROM users WHERE id = #{id}")
    User findById(@Param("id") UUID id);

    @Delete("DELETE FROM users WHERE id = #{id}")
    void delete(@Param("id") UUID id);

    @Insert("INSERT INTO users (email, password) VALUES (#{email}, #{password})")
    void addUser(User user);

    @Update("UPDATE users SET email=#{user.email} WHERE id=#{id}")
    void updateUser(@Param("id") UUID id, @Param("user")  User user);
}
