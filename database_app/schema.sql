--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.8
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accounts_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user (
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    email character varying(254) NOT NULL,
    username character varying(40) NOT NULL,
    fullname character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    date_joined date NOT NULL,
    is_verified boolean NOT NULL,
    card_id character varying(20) NOT NULL,
    contact character varying(255) NOT NULL,
    institution character varying(100) NOT NULL,
    phone_number character varying(15),
    last_notified_message timestamp with time zone NOT NULL
);


--
-- Name: accounts_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user_groups (
    id integer NOT NULL,
    user_id character varying(40) NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: accounts_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.accounts_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: accounts_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.accounts_user_groups_id_seq OWNED BY public.accounts_user_groups.id;


--
-- Name: accounts_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user_user_permissions (
    id integer NOT NULL,
    user_id character varying(40) NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: accounts_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.accounts_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: accounts_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.accounts_user_user_permissions_id_seq OWNED BY public.accounts_user_user_permissions.id;


--
-- Name: accounts_userfollow; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_userfollow (
    id integer NOT NULL,
    date_followed timestamp with time zone NOT NULL,
    who_id character varying(40) NOT NULL,
    whom_id character varying(40) NOT NULL
);


--
-- Name: accounts_userfollow_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.accounts_userfollow_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: accounts_userfollow_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.accounts_userfollow_id_seq OWNED BY public.accounts_userfollow.id;


--
-- Name: activity_activity; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_activity (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    photo character varying(100) NOT NULL,
    description text NOT NULL,
    location_latitude double precision NOT NULL,
    location_longitude double precision NOT NULL,
    location_name character varying(64) NOT NULL,
    fee integer NOT NULL,
    maximum_guest integer NOT NULL,
    date_held date NOT NULL,
    "time" time without time zone NOT NULL,
    duration integer NOT NULL,
    status character varying(16) NOT NULL,
    partner_id character varying(40) NOT NULL,
    caption text NOT NULL
);


--
-- Name: activity_activity_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_activity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_activity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_activity_id_seq OWNED BY public.activity_activity.id;


--
-- Name: activity_activity_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_activity_tags (
    id integer NOT NULL,
    activity_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: activity_activity_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_activity_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_activity_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_activity_tags_id_seq OWNED BY public.activity_activity_tags.id;


--
-- Name: activity_comment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_comment (
    id integer NOT NULL,
    text text NOT NULL,
    created_date timestamp with time zone NOT NULL,
    activity_id integer NOT NULL,
    user_id character varying(40) NOT NULL
);


--
-- Name: activity_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_comment_id_seq OWNED BY public.activity_comment.id;


--
-- Name: activity_like; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_like (
    id integer NOT NULL,
    activity_id integer NOT NULL,
    user_id character varying(40) NOT NULL
);


--
-- Name: activity_like_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_like_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_like_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_like_id_seq OWNED BY public.activity_like.id;


--
-- Name: activity_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_tag (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    slug character varying(50) NOT NULL
);


--
-- Name: activity_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_tag_id_seq OWNED BY public.activity_tag.id;


--
-- Name: activity_userjoinactivity; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.activity_userjoinactivity (
    id integer NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    activity_id integer NOT NULL,
    guest_id character varying(40) NOT NULL
);


--
-- Name: activity_userjoinactivity_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.activity_userjoinactivity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: activity_userjoinactivity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.activity_userjoinactivity_id_seq OWNED BY public.activity_userjoinactivity.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id character varying(40) NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: kelas_bookedclass; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_bookedclass (
    id integer NOT NULL,
    date timestamp with time zone NOT NULL,
    additional_description text,
    status character varying(16) NOT NULL,
    open_class_id integer
);


--
-- Name: kelas_bookedclass_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_bookedclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_bookedclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_bookedclass_id_seq OWNED BY public.kelas_bookedclass.id;


--
-- Name: kelas_bookedclass_users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_bookedclass_users (
    id integer NOT NULL,
    bookedclass_id integer NOT NULL,
    user_id character varying(40) NOT NULL
);


--
-- Name: kelas_bookedclass_users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_bookedclass_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_bookedclass_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_bookedclass_users_id_seq OWNED BY public.kelas_bookedclass_users.id;


--
-- Name: kelas_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_category (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    slug character varying(50) NOT NULL
);


--
-- Name: kelas_category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_category_id_seq OWNED BY public.kelas_category.id;


--
-- Name: kelas_openclass; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_openclass (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    description text NOT NULL,
    location_latitude double precision NOT NULL,
    location_longitude double precision NOT NULL,
    location_name character varying(64) NOT NULL,
    location_description text,
    is_active boolean NOT NULL,
    partner_id character varying(40) NOT NULL,
    fee integer,
    maximum_guest integer
);


--
-- Name: kelas_openclass_categories; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_openclass_categories (
    id integer NOT NULL,
    openclass_id integer NOT NULL,
    category_id integer NOT NULL
);


--
-- Name: kelas_openclass_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_openclass_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_openclass_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_openclass_categories_id_seq OWNED BY public.kelas_openclass_categories.id;


--
-- Name: kelas_openclass_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_openclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_openclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_openclass_id_seq OWNED BY public.kelas_openclass.id;


--
-- Name: kelas_openclass_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_openclass_tags (
    id integer NOT NULL,
    openclass_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: kelas_openclass_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_openclass_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_openclass_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_openclass_tags_id_seq OWNED BY public.kelas_openclass_tags.id;


--
-- Name: kelas_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.kelas_tag (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    slug character varying(50) NOT NULL
);


--
-- Name: kelas_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.kelas_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: kelas_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.kelas_tag_id_seq OWNED BY public.kelas_tag.id;


--
-- Name: profiles_profile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.profiles_profile (
    user_id character varying(40) NOT NULL,
    avatar character varying(100) NOT NULL,
    bio character varying(200) NOT NULL
);


--
-- Name: usermessages_usermessage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usermessages_usermessage (
    id integer NOT NULL,
    date_sent timestamp with time zone NOT NULL,
    message text NOT NULL,
    receiver_id character varying(40) NOT NULL,
    sender_id character varying(40) NOT NULL
);


--
-- Name: usermessages_usermessage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usermessages_usermessage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usermessages_usermessage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usermessages_usermessage_id_seq OWNED BY public.usermessages_usermessage.id;


--
-- Name: accounts_user_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups ALTER COLUMN id SET DEFAULT nextval('public.accounts_user_groups_id_seq'::regclass);


--
-- Name: accounts_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.accounts_user_user_permissions_id_seq'::regclass);


--
-- Name: accounts_userfollow id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_userfollow ALTER COLUMN id SET DEFAULT nextval('public.accounts_userfollow_id_seq'::regclass);


--
-- Name: activity_activity id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity ALTER COLUMN id SET DEFAULT nextval('public.activity_activity_id_seq'::regclass);


--
-- Name: activity_activity_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity_tags ALTER COLUMN id SET DEFAULT nextval('public.activity_activity_tags_id_seq'::regclass);


--
-- Name: activity_comment id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_comment ALTER COLUMN id SET DEFAULT nextval('public.activity_comment_id_seq'::regclass);


--
-- Name: activity_like id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_like ALTER COLUMN id SET DEFAULT nextval('public.activity_like_id_seq'::regclass);


--
-- Name: activity_tag id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_tag ALTER COLUMN id SET DEFAULT nextval('public.activity_tag_id_seq'::regclass);


--
-- Name: activity_userjoinactivity id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_userjoinactivity ALTER COLUMN id SET DEFAULT nextval('public.activity_userjoinactivity_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: kelas_bookedclass id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass ALTER COLUMN id SET DEFAULT nextval('public.kelas_bookedclass_id_seq'::regclass);


--
-- Name: kelas_bookedclass_users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass_users ALTER COLUMN id SET DEFAULT nextval('public.kelas_bookedclass_users_id_seq'::regclass);


--
-- Name: kelas_category id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_category ALTER COLUMN id SET DEFAULT nextval('public.kelas_category_id_seq'::regclass);


--
-- Name: kelas_openclass id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass ALTER COLUMN id SET DEFAULT nextval('public.kelas_openclass_id_seq'::regclass);


--
-- Name: kelas_openclass_categories id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_categories ALTER COLUMN id SET DEFAULT nextval('public.kelas_openclass_categories_id_seq'::regclass);


--
-- Name: kelas_openclass_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_tags ALTER COLUMN id SET DEFAULT nextval('public.kelas_openclass_tags_id_seq'::regclass);


--
-- Name: kelas_tag id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_tag ALTER COLUMN id SET DEFAULT nextval('public.kelas_tag_id_seq'::regclass);


--
-- Name: usermessages_usermessage id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usermessages_usermessage ALTER COLUMN id SET DEFAULT nextval('public.usermessages_usermessage_id_seq'::regclass);


--
-- Name: accounts_user accounts_user_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user
    ADD CONSTRAINT accounts_user_email_key UNIQUE (email);


--
-- Name: accounts_user_groups accounts_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_groups accounts_user_groups_user_id_59c0b32f_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_user_id_59c0b32f_uniq UNIQUE (user_id, group_id);


--
-- Name: accounts_user accounts_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user
    ADD CONSTRAINT accounts_user_pkey PRIMARY KEY (username);


--
-- Name: accounts_user_user_permissions accounts_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_user_permissions accounts_user_user_permissions_user_id_2ab516c2_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_permissions_user_id_2ab516c2_uniq UNIQUE (user_id, permission_id);


--
-- Name: accounts_userfollow accounts_userfollow_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_userfollow
    ADD CONSTRAINT accounts_userfollow_pkey PRIMARY KEY (id);


--
-- Name: accounts_userfollow accounts_userfollow_who_id_8fece4fb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_userfollow
    ADD CONSTRAINT accounts_userfollow_who_id_8fece4fb_uniq UNIQUE (who_id, whom_id);


--
-- Name: activity_activity activity_activity_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity
    ADD CONSTRAINT activity_activity_pkey PRIMARY KEY (id);


--
-- Name: activity_activity_tags activity_activity_tags_activity_id_25afe447_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity_tags
    ADD CONSTRAINT activity_activity_tags_activity_id_25afe447_uniq UNIQUE (activity_id, tag_id);


--
-- Name: activity_activity_tags activity_activity_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity_tags
    ADD CONSTRAINT activity_activity_tags_pkey PRIMARY KEY (id);


--
-- Name: activity_comment activity_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_comment
    ADD CONSTRAINT activity_comment_pkey PRIMARY KEY (id);


--
-- Name: activity_like activity_like_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_like
    ADD CONSTRAINT activity_like_pkey PRIMARY KEY (id);


--
-- Name: activity_like activity_like_user_id_a152b4b7_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_like
    ADD CONSTRAINT activity_like_user_id_a152b4b7_uniq UNIQUE (user_id, activity_id);


--
-- Name: activity_tag activity_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_tag
    ADD CONSTRAINT activity_tag_pkey PRIMARY KEY (id);


--
-- Name: activity_userjoinactivity activity_userjoinactivity_guest_id_52c05257_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_userjoinactivity
    ADD CONSTRAINT activity_userjoinactivity_guest_id_52c05257_uniq UNIQUE (guest_id, activity_id);


--
-- Name: activity_userjoinactivity activity_userjoinactivity_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_userjoinactivity
    ADD CONSTRAINT activity_userjoinactivity_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: kelas_bookedclass kelas_bookedclass_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass
    ADD CONSTRAINT kelas_bookedclass_pkey PRIMARY KEY (id);


--
-- Name: kelas_bookedclass_users kelas_bookedclass_users_bookedclass_id_d563b680_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass_users
    ADD CONSTRAINT kelas_bookedclass_users_bookedclass_id_d563b680_uniq UNIQUE (bookedclass_id, user_id);


--
-- Name: kelas_bookedclass_users kelas_bookedclass_users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass_users
    ADD CONSTRAINT kelas_bookedclass_users_pkey PRIMARY KEY (id);


--
-- Name: kelas_category kelas_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_category
    ADD CONSTRAINT kelas_category_pkey PRIMARY KEY (id);


--
-- Name: kelas_openclass_categories kelas_openclass_categories_openclass_id_fca4effd_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_categories
    ADD CONSTRAINT kelas_openclass_categories_openclass_id_fca4effd_uniq UNIQUE (openclass_id, category_id);


--
-- Name: kelas_openclass_categories kelas_openclass_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_categories
    ADD CONSTRAINT kelas_openclass_categories_pkey PRIMARY KEY (id);


--
-- Name: kelas_openclass kelas_openclass_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass
    ADD CONSTRAINT kelas_openclass_pkey PRIMARY KEY (id);


--
-- Name: kelas_openclass_tags kelas_openclass_tags_openclass_id_54681995_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_tags
    ADD CONSTRAINT kelas_openclass_tags_openclass_id_54681995_uniq UNIQUE (openclass_id, tag_id);


--
-- Name: kelas_openclass_tags kelas_openclass_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_tags
    ADD CONSTRAINT kelas_openclass_tags_pkey PRIMARY KEY (id);


--
-- Name: kelas_tag kelas_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_tag
    ADD CONSTRAINT kelas_tag_pkey PRIMARY KEY (id);


--
-- Name: profiles_profile profiles_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profiles_profile
    ADD CONSTRAINT profiles_profile_pkey PRIMARY KEY (user_id);


--
-- Name: usermessages_usermessage usermessages_usermessage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usermessages_usermessage
    ADD CONSTRAINT usermessages_usermessage_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_email_b2644a56_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_email_b2644a56_like ON public.accounts_user USING btree (email varchar_pattern_ops);


--
-- Name: accounts_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_groups_0e939a4f ON public.accounts_user_groups USING btree (group_id);


--
-- Name: accounts_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_groups_e8701ad4 ON public.accounts_user_groups USING btree (user_id);


--
-- Name: accounts_user_groups_user_id_52b62117_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_groups_user_id_52b62117_like ON public.accounts_user_groups USING btree (user_id varchar_pattern_ops);


--
-- Name: accounts_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_user_permissions_8373b171 ON public.accounts_user_user_permissions USING btree (permission_id);


--
-- Name: accounts_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_user_permissions_e8701ad4 ON public.accounts_user_user_permissions USING btree (user_id);


--
-- Name: accounts_user_user_permissions_user_id_e4f0a161_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_user_permissions_user_id_e4f0a161_like ON public.accounts_user_user_permissions USING btree (user_id varchar_pattern_ops);


--
-- Name: accounts_user_username_6088629e_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_username_6088629e_like ON public.accounts_user USING btree (username varchar_pattern_ops);


--
-- Name: accounts_userfollow_0f356e71; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_userfollow_0f356e71 ON public.accounts_userfollow USING btree (whom_id);


--
-- Name: accounts_userfollow_ec8016b5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_userfollow_ec8016b5 ON public.accounts_userfollow USING btree (who_id);


--
-- Name: accounts_userfollow_who_id_7dfbbc4f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_userfollow_who_id_7dfbbc4f_like ON public.accounts_userfollow USING btree (who_id varchar_pattern_ops);


--
-- Name: accounts_userfollow_whom_id_38d26046_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_userfollow_whom_id_38d26046_like ON public.accounts_userfollow USING btree (whom_id varchar_pattern_ops);


--
-- Name: activity_activity_4e98b6eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_activity_4e98b6eb ON public.activity_activity USING btree (partner_id);


--
-- Name: activity_activity_partner_id_537b77b0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_activity_partner_id_537b77b0_like ON public.activity_activity USING btree (partner_id varchar_pattern_ops);


--
-- Name: activity_activity_tags_76f094bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_activity_tags_76f094bc ON public.activity_activity_tags USING btree (tag_id);


--
-- Name: activity_activity_tags_f8a3193a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_activity_tags_f8a3193a ON public.activity_activity_tags USING btree (activity_id);


--
-- Name: activity_comment_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_comment_e8701ad4 ON public.activity_comment USING btree (user_id);


--
-- Name: activity_comment_f8a3193a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_comment_f8a3193a ON public.activity_comment USING btree (activity_id);


--
-- Name: activity_comment_user_id_08a4569f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_comment_user_id_08a4569f_like ON public.activity_comment USING btree (user_id varchar_pattern_ops);


--
-- Name: activity_like_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_like_e8701ad4 ON public.activity_like USING btree (user_id);


--
-- Name: activity_like_f8a3193a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_like_f8a3193a ON public.activity_like USING btree (activity_id);


--
-- Name: activity_like_user_id_2739822f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_like_user_id_2739822f_like ON public.activity_like USING btree (user_id varchar_pattern_ops);


--
-- Name: activity_tag_2dbcba41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_tag_2dbcba41 ON public.activity_tag USING btree (slug);


--
-- Name: activity_tag_slug_4610b880_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_tag_slug_4610b880_like ON public.activity_tag USING btree (slug varchar_pattern_ops);


--
-- Name: activity_userjoinactivity_64701d7f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_userjoinactivity_64701d7f ON public.activity_userjoinactivity USING btree (guest_id);


--
-- Name: activity_userjoinactivity_f8a3193a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_userjoinactivity_f8a3193a ON public.activity_userjoinactivity USING btree (activity_id);


--
-- Name: activity_userjoinactivity_guest_id_b234cb2c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX activity_userjoinactivity_guest_id_b234cb2c_like ON public.activity_userjoinactivity USING btree (guest_id varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_0e939a4f ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_8373b171 ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_417f1b1c ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_417f1b1c ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_e8701ad4 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_admin_log_user_id_c564eba6_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6_like ON public.django_admin_log USING btree (user_id varchar_pattern_ops);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_de54fa62 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: kelas_bookedclass_a0924a80; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_bookedclass_a0924a80 ON public.kelas_bookedclass USING btree (open_class_id);


--
-- Name: kelas_bookedclass_users_b82a61c3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_bookedclass_users_b82a61c3 ON public.kelas_bookedclass_users USING btree (bookedclass_id);


--
-- Name: kelas_bookedclass_users_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_bookedclass_users_e8701ad4 ON public.kelas_bookedclass_users USING btree (user_id);


--
-- Name: kelas_bookedclass_users_user_id_75c32bfa_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_bookedclass_users_user_id_75c32bfa_like ON public.kelas_bookedclass_users USING btree (user_id varchar_pattern_ops);


--
-- Name: kelas_category_2dbcba41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_category_2dbcba41 ON public.kelas_category USING btree (slug);


--
-- Name: kelas_category_slug_3415ac47_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_category_slug_3415ac47_like ON public.kelas_category USING btree (slug varchar_pattern_ops);


--
-- Name: kelas_openclass_4e98b6eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_4e98b6eb ON public.kelas_openclass USING btree (partner_id);


--
-- Name: kelas_openclass_categories_b4e33e1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_categories_b4e33e1c ON public.kelas_openclass_categories USING btree (openclass_id);


--
-- Name: kelas_openclass_categories_b583a629; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_categories_b583a629 ON public.kelas_openclass_categories USING btree (category_id);


--
-- Name: kelas_openclass_partner_id_8ca40adb_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_partner_id_8ca40adb_like ON public.kelas_openclass USING btree (partner_id varchar_pattern_ops);


--
-- Name: kelas_openclass_tags_76f094bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_tags_76f094bc ON public.kelas_openclass_tags USING btree (tag_id);


--
-- Name: kelas_openclass_tags_b4e33e1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_openclass_tags_b4e33e1c ON public.kelas_openclass_tags USING btree (openclass_id);


--
-- Name: kelas_tag_2dbcba41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_tag_2dbcba41 ON public.kelas_tag USING btree (slug);


--
-- Name: kelas_tag_slug_735a86a9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX kelas_tag_slug_735a86a9_like ON public.kelas_tag USING btree (slug varchar_pattern_ops);


--
-- Name: profiles_profile_user_id_a3e81f91_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX profiles_profile_user_id_a3e81f91_like ON public.profiles_profile USING btree (user_id varchar_pattern_ops);


--
-- Name: usermessages_usermessage_924b1846; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX usermessages_usermessage_924b1846 ON public.usermessages_usermessage USING btree (sender_id);


--
-- Name: usermessages_usermessage_d41c2251; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX usermessages_usermessage_d41c2251 ON public.usermessages_usermessage USING btree (receiver_id);


--
-- Name: usermessages_usermessage_receiver_id_0af3b3fd_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX usermessages_usermessage_receiver_id_0af3b3fd_like ON public.usermessages_usermessage USING btree (receiver_id varchar_pattern_ops);


--
-- Name: usermessages_usermessage_sender_id_76c5fdef_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX usermessages_usermessage_sender_id_76c5fdef_like ON public.usermessages_usermessage USING btree (sender_id varchar_pattern_ops);


--
-- Name: accounts_user_groups accounts_user_groups_group_id_bd11a704_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_group_id_bd11a704_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_groups accounts_user_groups_user_id_52b62117_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_user_id_52b62117_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_user_permissions accounts_user_user_p_user_id_e4f0a161_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_p_user_id_e4f0a161_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_user_permissions accounts_user_user_permission_id_113bb443_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_permission_id_113bb443_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_userfollow accounts_userfollow_who_id_7dfbbc4f_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_userfollow
    ADD CONSTRAINT accounts_userfollow_who_id_7dfbbc4f_fk_accounts_user_username FOREIGN KEY (who_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_userfollow accounts_userfollow_whom_id_38d26046_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_userfollow
    ADD CONSTRAINT accounts_userfollow_whom_id_38d26046_fk_accounts_user_username FOREIGN KEY (whom_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_activity activity_activi_partner_id_537b77b0_fk_profiles_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity
    ADD CONSTRAINT activity_activi_partner_id_537b77b0_fk_profiles_profile_user_id FOREIGN KEY (partner_id) REFERENCES public.profiles_profile(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_activity_tags activity_activity__activity_id_6342e9b5_fk_activity_activity_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity_tags
    ADD CONSTRAINT activity_activity__activity_id_6342e9b5_fk_activity_activity_id FOREIGN KEY (activity_id) REFERENCES public.activity_activity(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_activity_tags activity_activity_tags_tag_id_091d98b3_fk_activity_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_activity_tags
    ADD CONSTRAINT activity_activity_tags_tag_id_091d98b3_fk_activity_tag_id FOREIGN KEY (tag_id) REFERENCES public.activity_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_comment activity_comment_activity_id_899d176d_fk_activity_activity_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_comment
    ADD CONSTRAINT activity_comment_activity_id_899d176d_fk_activity_activity_id FOREIGN KEY (activity_id) REFERENCES public.activity_activity(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_comment activity_comment_user_id_08a4569f_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_comment
    ADD CONSTRAINT activity_comment_user_id_08a4569f_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_like activity_like_activity_id_4879b024_fk_activity_activity_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_like
    ADD CONSTRAINT activity_like_activity_id_4879b024_fk_activity_activity_id FOREIGN KEY (activity_id) REFERENCES public.activity_activity(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_like activity_like_user_id_2739822f_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_like
    ADD CONSTRAINT activity_like_user_id_2739822f_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_userjoinactivity activity_userjoina_activity_id_b9da5f31_fk_activity_activity_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_userjoinactivity
    ADD CONSTRAINT activity_userjoina_activity_id_b9da5f31_fk_activity_activity_id FOREIGN KEY (activity_id) REFERENCES public.activity_activity(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_userjoinactivity activity_userjoinac_guest_id_b234cb2c_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.activity_userjoinactivity
    ADD CONSTRAINT activity_userjoinac_guest_id_b234cb2c_fk_accounts_user_username FOREIGN KEY (guest_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_bookedclass_users kelas_bookedcla_bookedclass_id_bb761d58_fk_kelas_bookedclass_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass_users
    ADD CONSTRAINT kelas_bookedcla_bookedclass_id_bb761d58_fk_kelas_bookedclass_id FOREIGN KEY (bookedclass_id) REFERENCES public.kelas_bookedclass(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_bookedclass kelas_bookedclass_open_class_id_e4a11603_fk_kelas_openclass_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass
    ADD CONSTRAINT kelas_bookedclass_open_class_id_e4a11603_fk_kelas_openclass_id FOREIGN KEY (open_class_id) REFERENCES public.kelas_openclass(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_bookedclass_users kelas_bookedclass_us_user_id_75c32bfa_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_bookedclass_users
    ADD CONSTRAINT kelas_bookedclass_us_user_id_75c32bfa_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_openclass_categories kelas_openclass_cat_openclass_id_e45e7b39_fk_kelas_openclass_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_categories
    ADD CONSTRAINT kelas_openclass_cat_openclass_id_e45e7b39_fk_kelas_openclass_id FOREIGN KEY (openclass_id) REFERENCES public.kelas_openclass(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_openclass_categories kelas_openclass_categ_category_id_65553556_fk_kelas_category_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_categories
    ADD CONSTRAINT kelas_openclass_categ_category_id_65553556_fk_kelas_category_id FOREIGN KEY (category_id) REFERENCES public.kelas_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_openclass kelas_openclass_partner_id_8ca40adb_fk_profiles_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass
    ADD CONSTRAINT kelas_openclass_partner_id_8ca40adb_fk_profiles_profile_user_id FOREIGN KEY (partner_id) REFERENCES public.profiles_profile(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_openclass_tags kelas_openclass_tag_openclass_id_26eb78ca_fk_kelas_openclass_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_tags
    ADD CONSTRAINT kelas_openclass_tag_openclass_id_26eb78ca_fk_kelas_openclass_id FOREIGN KEY (openclass_id) REFERENCES public.kelas_openclass(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kelas_openclass_tags kelas_openclass_tags_tag_id_598af154_fk_kelas_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.kelas_openclass_tags
    ADD CONSTRAINT kelas_openclass_tags_tag_id_598af154_fk_kelas_tag_id FOREIGN KEY (tag_id) REFERENCES public.kelas_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: profiles_profile profiles_profile_user_id_a3e81f91_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profiles_profile
    ADD CONSTRAINT profiles_profile_user_id_a3e81f91_fk_accounts_user_username FOREIGN KEY (user_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usermessages_usermessage usermessages_use_receiver_id_0af3b3fd_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usermessages_usermessage
    ADD CONSTRAINT usermessages_use_receiver_id_0af3b3fd_fk_accounts_user_username FOREIGN KEY (receiver_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usermessages_usermessage usermessages_userm_sender_id_76c5fdef_fk_accounts_user_username; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usermessages_usermessage
    ADD CONSTRAINT usermessages_userm_sender_id_76c5fdef_fk_accounts_user_username FOREIGN KEY (sender_id) REFERENCES public.accounts_user(username) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

