import { describe, expect, test } from '@jest/globals';
import $ from 'jquery';
import 'slick-carousel';
import 'aofsr';

describe('main.js', () => {
    test('should initialize slick slider', () => {
        const slickSpy = jest.spyOn($.fn, 'slick');
        document.body.innerHTML = '<div class="slider"></div>';

        $('.slider').slick({
            autoplay: true,
            infinite: true,
            speed: 300,
            slidesToShow: 3,
            centerMode: true,
            centerPadding: '60px',
            variableWidth: true,
        });

        expect(slickSpy).toHaveBeenCalled();
    });

    test('should initialize aofsr', () => {
        const aofsrSpy = jest.spyOn($.fn, 'aofsr');
        document.body.innerHTML = '<div class="job-title"></div>';

        $('.job-title').aofsr({
            phraseMode: true,
        });

        expect(aofsrSpy).toHaveBeenCalled();
    });
});