import { describe, expect, test } from '@jest/globals';
import { JSDOM } from 'jsdom';
import { loadImage } from './profile';

describe('loadImage function', () => {
    let dom;
    let input;
    let profileImage;

    beforeEach(() => {
        dom = new JSDOM('<html><body><input type="file" id="fileInput"><img id="profileImage"></body></html>');
        global.window = dom.window;
        global.document = dom.window.document;
        input = document.getElementById('fileInput');
        profileImage = document.getElementById('profileImage');
    });

    afterEach(() => {
        delete global.window;
        delete global.document;
    });

    test('should set the src attribute of profileImage', () => {
        const file = new File([''], 'test.png', { type: 'image/png' });
        const reader = new FileReader();
        const dataUrl = 'data:image/png;base64,';
        reader.onload = () => {
            profileImage.onload = () => {
                expect(profileImage.src).toBe(dataUrl);
            };
            profileImage.onerror = () => {
                throw new Error('Failed to load image');
            };
            profileImage.src = reader.result;
        };
        reader.readAsDataURL(file);

        loadImage(input);
    });

    test('should not set the src attribute of profileImage if no file is selected', () => {
        const spy = jest.spyOn(profileImage, 'setAttribute');

        loadImage(input);

        expect(spy).not.toHaveBeenCalled();
    });
});