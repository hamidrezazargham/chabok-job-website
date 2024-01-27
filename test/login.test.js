import { login } from './login';

describe('login function', () => {
    it('should call the backend endpoint with the given email and password', () => {
        const email = 'test@test.com';
        const password = 'password';
        const formData = { email, password };
        const ajaxSpy = jest.spyOn($, 'ajax').mockImplementation(() => {});

        login(email, password);

        expect(ajaxSpy).toHaveBeenCalledWith({
            url: 'https://c042-109-230-67-162.ngrok-free.app/login/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: expect.any(Function),
            error: expect.any(Function),
        });
    });
});