insert into
    "EVERYTHING_CORONA_PARTITION_TEST"(
        SELECT
            *
        FROM
            "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA"
        GROUP BY
            date_parsed_formatted
    );
