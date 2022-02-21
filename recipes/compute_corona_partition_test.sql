insert into
    "PUBLIC"."${projectKey}_SNOWFLAKE_CORONA_COPY"(
        SELECT
            *
        FROM
            "PUBLIC"."${projectKey}_SNOWFLAKE_CORONA"
    );





