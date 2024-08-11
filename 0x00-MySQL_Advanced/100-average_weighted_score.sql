--  a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a studentDELIMITER $$
-- Weighted average= ∑(Value×Weight) / ∑Weight

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id int)
BEGIN
    DECLARE weight_sum float;
    DECLARE weighted_score_sum float;
    DECLARE weighted_average float;

    SELECT SUM(projects.weight)
    INTO weight_sum
    FROM projects
    INNER JOIN corrections on corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    SELECT SUM(corrections.score * projects.weight)
    INTO weighted_score_sum
    FROM corrections
    INNER JOIN projects on corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    IF weight_sum > 0 THEN
        SET weighted_average = weighted_score_sum / weight_sum;
    ELSE
        SET weighted_average = 0;
    END IF;

    UPDATE users
    SET average_score = weighted_average
    WHERE id = user_id;
END $$

DELIMITER ;
