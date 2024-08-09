-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN
    DECLARE av_score float;
    SELECT AVG(score) INTO av_score
    FROM corrections
    WHERE corrections.user_id = user_id; 
    UPDATE users
    SET average_score = av_score
    WHERE id = user_id;
END $$

DELIMITER ;
