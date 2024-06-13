package com.dev.flashcards.mapper;

import com.dev.flashcards.model.Role;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.UUID;

@Mapper
public interface RoleMapper {
    @Select("SELECT * FROM roles WHERE name = #{name}")
    Role findByName(@Param("name") String name);

    @Select("SELECT * FROM roles WHERE id = #{id}")
    Role findById(@Param("id") UUID id);

    @Insert("INSERT INTO user_roles (user_id, role_id) VALUES (#{userId}, #{roleId})")
    void addRoleToUser(@Param("userId") UUID userId, @Param("roleId") UUID roleId);

}
