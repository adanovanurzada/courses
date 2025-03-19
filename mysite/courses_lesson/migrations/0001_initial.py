# Generated by Django 5.1.7 on 2025-03-18 10:02

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('client', 'client'), ('teacher', 'teacher'), ('administrator', 'administrator')], default='client', max_length=15)),
                ('full_name', models.CharField(max_length=34)),
                ('profile_picture', models.ImageField(upload_to='profile_picture/')),
                ('bio', models.TextField()),
                ('groups', models.ManyToManyField(blank=True, related_name='user_profiles_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_profiles_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=34)),
                ('course_name_en', models.CharField(max_length=34, null=True)),
                ('course_name_ru', models.CharField(max_length=34, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Inter', 'Inter'), ('Adverse', 'Adverse')], default='beginner', max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_lesson.category')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exam', models.CharField(max_length=32)),
                ('name_exam_en', models.CharField(max_length=32, null=True)),
                ('name_exam_ru', models.CharField(max_length=32, null=True)),
                ('passing_score', models.PositiveSmallIntegerField()),
                ('duration', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_lesson.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=32)),
                ('name_lesson_en', models.CharField(max_length=32, null=True)),
                ('name_lesson_ru', models.CharField(max_length=32, null=True)),
                ('video_url', models.URLField()),
                ('content', models.TextField(blank=True, null=True)),
                ('content_en', models.TextField(blank=True, null=True)),
                ('content_ru', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_course', to='courses_lesson.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_questions', models.CharField(max_length=32)),
                ('name_questions_en', models.CharField(max_length=32, null=True)),
                ('name_questions_ru', models.CharField(max_length=32, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_lesson.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=64)),
                ('answers_en', models.CharField(max_length=64, null=True)),
                ('answers_ru', models.CharField(max_length=64, null=True)),
                ('true_answers', models.BooleanField(default=False)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_lesson.question')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses_lesson.userprofile')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('courses_lesson.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses_lesson.userprofile')),
                ('experience', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('courses_lesson.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField()),
                ('comment_en', models.TextField(null=True)),
                ('comment_ru', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_review', to='courses_lesson.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='courses_lesson.student')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links_url', models.URLField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links_student', to='courses_lesson.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateField(auto_now_add=True)),
                ('certificate_file', models.FileField(upload_to='certificate_file')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_certificate', to='courses_lesson.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_certificate', to='courses_lesson.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_assignment', models.CharField(max_length=32)),
                ('name_assignment_en', models.CharField(max_length=32, null=True)),
                ('name_assignment_ru', models.CharField(max_length=32, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('due_date', models.DateTimeField()),
                ('students', models.ManyToManyField(related_name='students', to='courses_lesson.userprofile')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_course', to='courses_lesson.student')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_lesson.teacher'),
        ),
    ]
