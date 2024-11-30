# Additional Research
![Pixel To Page](images/Placeholder.png)

<p align="center">
| <a href="https://pixel-to-page-b4e4b9d4d8dd.herokuapp.com/">Live Project</a> |
  <a href="https://github.com/users/TheRickyroy/projects/3">Project Board</a> |
  <a href="https://github.com/TheRickyroy/pixel-to-page/blob/main/README.md">README</a> |
  <a href="https://github.com/TheRickyroy/pixel-to-page/blob/main/documentation/testing.md">Testing & Validation</a> |
</p>

## Table of Contents  
  
- [Additional Research](#additional-research)
  - [Table of Contents](#table-of-contents)
- [Color](#color)
  - [Color Space](#color-space)





## Color

### Color Space

>Personally, I'm using HSL. In the coming months, I plan on migrating to OKLCH, but it feels just a bit too bleeding-edge at the moment.
>
> [Josh W Comeau](https://www.joshwcomeau.com/css/color-formats/)

> But, that being said, OKLCH comes with two challenges:
>
> With OKLCH and LCH, not all combinations of L, C, and H will result in colors that are supported by every monitor. Although browsers will try to find the closest supported color, it’s still safer to check colors using our color picker.
>
>OKLCH is a new color space. At the time of this writing in 2024, its ecosystem is still limited (for Figma we have the plugin but not official support), but we already have a palette generator, color picker, and many converters.
>
>[Evil Martians](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)

<br><details><summary>MDN Web Docs - lab()</summary>

[mdn web docs_lab()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lab)

![mdn Browser Compatibility](images/research/mdn-lab.png)

</details><br>

<details><summary>MDN Web Docs - lch()</summary>

[mdn web docs_lch()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lch)

![mdn Browser Compatibility](images/research/mdn-lch.png)

</details><br>


Reading Material

- [Atoms - LCH is the best color space for UI](https://atmos.style/blog/lch-color-space)
- [Atmos - HEX to LCH Color Converter](https://atmos.style/color-converter/hex-to-lch)
- [Can I Use - LCH and Lab color values](https://caniuse.com/css-lch-lab)
- [Evil Martians - OKLCH in CSS: why we moved from RGB and HSL](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)
- [Josh W. Comeau - Color Formats in CSS](https://www.joshwcomeau.com/css/color-formats/)
- [Lambdatest - LCH and Lab color values](https://www.lambdatest.com/web-technologies/css-lch-lab)
- [Lea Verou - LCH colors in CSS: what, why, and how?](https://lea.verou.me/blog/2020/04/lch-colors-in-css-what-why-and-how/)
- [MDN - lab()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lab)
- [MDN - lch()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lch)
- [Smashing Magazine - A Guide To Modern CSS Colors With RGB, HSL, HWB, LAB And LCH](https://www.smashingmagazine.com/2021/11/guide-modern-css-colors/)
