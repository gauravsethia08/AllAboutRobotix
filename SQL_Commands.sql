# ----- Account App -------
BEGIN;
--
-- Remove field num_course_completed from user
--
CREATE TABLE "new__account_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "name" varchar(254) NULL, "institution" varchar(50) NOT NULL, "github" varchar(50) NOT NULL, "address" varchar(200) NOT NULL, "city" varchar(20) NOT NULL, "country" varchar(30) NOT NULL, "profile_img" varchar(100) NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL, "is_active" bool NOT NULL, "last_login" datetime NULL, "date_joined" datetime NOT NULL, "num_course_taken" integer NOT NULL);
INSERT INTO "new__account_user" ("id", "password", "email", "name", "institution", "github", "address", "city", "country", "profile_img", "is_staff", "is_superuser", "is_active", "last_login", "date_joined", "num_course_taken") SELECT "id", "password", "email", "name", "institution", "github", "address", "city", "country", "profile_img", "is_staff", "is_superuser", "is_active", "last_login", "date_joined", "num_course_taken" FROM "account_user";
DROP TABLE "account_user";
ALTER TABLE "new__account_user" RENAME TO "account_user";
--
-- Remove field num_course_taken from user
--
CREATE TABLE "new__account_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "name" varchar(254) NULL, "institution" varchar(50) NOT NULL, "github" varchar(50) NOT NULL, "address" varchar(200) NOT NULL, "city" varchar(20) NOT NULL, "country" varchar(30) NOT NULL, "profile_img" varchar(100) NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL, "is_active" bool NOT NULL, "last_login" datetime NULL, "date_joined" datetime NOT NULL);
INSERT INTO "new__account_user" ("id", "password", "email", "name", "institution", "github", "address", "city", "country", "profile_img", "is_staff", "is_superuser", "is_active", "last_login", "date_joined") SELECT "id", "password", "email", "name", "institution", "github", "address", "city", "country", "profile_img", "is_staff", "is_superuser", "is_active", "last_login", "date_joined" FROM "account_user";
DROP TABLE "account_user";
ALTER TABLE "new__account_user" RENAME TO "account_user";
--
-- Alter field status on learning_progress
--
CREATE TABLE "new__account_learning_progress" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" integer NOT NULL, "enroll_id_id" integer NOT NULL REFERENCES "account_enrollment" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__account_learning_progress" ("id", "enroll_id_id", "status") SELECT "id", "enroll_id_id", "status" FROM "account_learning_progress";
DROP TABLE "account_learning_progress";
ALTER TABLE "new__account_learning_progress" RENAME TO "account_learning_progress";
CREATE INDEX "account_learning_progress_enroll_id_id_07c147c4" ON "account_learning_progress" ("enroll_id_id");
COMMIT;


# ------- Blog App --------
BEGIN;
--
-- Create model Blog
--
CREATE TABLE "blog_blog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL UNIQUE, "abstract" varchar(500) NOT NULL, "img" varchar(100) NOT NULL, "content" text NOT NULL, "blog_type" varchar(200) NOT NULL, "date_posted" datetime NOT NULL, "make_public" bool NOT NULL);
--
-- Create model subscribe
--
CREATE TABLE "blog_subscribe" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(254) NOT NULL);
--
-- Create model BlogComment
--
CREATE TABLE "blog_blogcomment" ("sno" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" text NOT NULL, "timestamp" datetime NOT NULL, "parent_id" integer NULL REFERENCES "blog_blogcomment" ("sno") DEFERRABLE INITIALLY DEFERRED, "post_id" integer NOT NULL REFERENCES "blog_blog" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "account_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_blogcomment_parent_id_df1e1d2a" ON "blog_blogcomment" ("parent_id");
CREATE INDEX "blog_blogcomment_post_id_f2a3e760" ON "blog_blogcomment" ("post_id");
CREATE INDEX "blog_blogcomment_user_id_dc3b3111" ON "blog_blogcomment" ("user_id");
COMMIT;


# -------- Courses App ---------
BEGIN;
--
-- Add field module_desc to module
--
CREATE TABLE "new__courses_module" ("module_desc" text NOT NULL, "module_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "moduel_no" integer NOT NULL, "no_text" integer NOT NULL, "no_videos" integer NOT NULL, "no_assignment" integer NOT NULL, "course_id" integer NOT NULL REFERENCES "courses_course" ("course_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__courses_module" ("module_id", "moduel_no", "no_text", "no_videos", "no_assignment", "course_id", "module_desc") SELECT "module_id", "moduel_no", "no_text", "no_videos", "no_assignment", "course_id", 'No Desc' FROM "courses_module";
DROP TABLE "courses_module";
ALTER TABLE "new__courses_module" RENAME TO "courses_module";
CREATE INDEX "courses_module_course_id_7d4820de" ON "courses_module" ("course_id");
--
-- Alter field course_title on course
--
CREATE TABLE "new__courses_course" ("course_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "course_descr" text NOT NULL, "no_modules" integer NOT NULL, "course_fee" real NOT NULL, "course_cover_img" varchar(100) NOT NULL, "course_title" varchar(20) NOT NULL UNIQUE);
INSERT INTO "new__courses_course" ("course_id", "course_descr", "no_modules", "course_fee", "course_cover_img", "course_title") SELECT "course_id", "course_descr", "no_modules", "course_fee", "course_cover_img", "course_title" FROM "courses_course";
DROP TABLE "courses_course";
ALTER TABLE "new__courses_course" RENAME TO "courses_course";
COMMIT;

# -------- Home App ---------
BEGIN;
--
-- Create model Contact
--
CREATE TABLE "home_page_contact" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(20) NOT NULL, "email" varchar(254) NOT NULL, "contact_no" varchar(15) NOT NULL, "message" text NOT NULL, "date" datetime NOT NULL);
COMMIT;