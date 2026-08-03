# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ReadingCircle
class UserSwitcher:
    def switch_profile(self, name: str) -> Optional[User]:
        for user in self.users.values():
            if user.name == name:
                return user
        raise ValueError(f"No such user: {name}")

    @property
    def current_user(self) -> User:
        return next(iter(self.profiles.values()))

    def activate_profile(self, profile_name: str) -> bool:
        if not self.profiles or profile_name not in self.profiles:
            return False
        self.current = profile_name
        return True

    @property
    def active_profiles(self) -> List[Profile]:
        return [self.profiles[p] for p in sorted(self.profiles.keys())]


def load_all_users(data: dict, store: UserStore):
    for name, u_data in data.items():
        user = User(**u_data)
        store.users[name] = user
        if not hasattr(store, '_profiles') or store._profiles is None:
            store.profiles = {}

    for profile_name, p_data in data.get('profiles', {}).items():
        profile = Profile.from_dict(p_data)
        store.profiles[profile_name] = profile
