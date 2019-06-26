-- 添加superuser
INSERT INTO auth_user (
  password,
  is_superuser, username, email, first_name, last_name, is_staff, is_active, date_joined
) VALUES (
  "pbkdf2_sha256$150000$p9sZVXszd6je$VhV3fyMmsh3uAsjOqcKBxNhZ9cGkQQS3bFsdc+jjANs=",
  1, "admin", "a@qq.com", "", "", 1, 1, 'now'
);
