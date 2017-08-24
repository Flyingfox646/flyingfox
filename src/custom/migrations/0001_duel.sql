ALTER TABLE online ADD COLUMN is_duel boolean;
ALTER TABLE online ALTER COLUMN is_duel SET NOT NULL;