import {createAuthProvider} from 'react-token-auth';

export const [useAuth, authFetch, login, logout] = createAuthProvider({
        accessTokenKey: "access",
        onUpdateToken: (token) => fetch("/auth/refresh", {
            method: "POST",
            body: token.refresh
        })
        .then(r => r.json())
    });