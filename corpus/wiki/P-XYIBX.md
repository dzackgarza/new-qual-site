---
schema: qual/card@1
id: P-XYIBX
kind: problem
title: "$\\displaystyle \\int \\frac {1 - \\sqrt {x}}{1 + \\sqrt {x}} ~dx = \\color{blue} {- x + 4 \\sqrt {x} - 4 \\ln (1 + x)}$ Solution: $u = 1 + \\sqrt {x}$, $x = (u - 1)^2$, $dx = 2(u - 1) ~du$"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
relations: []
review: draft
---

1. $\displaystyle \int \frac {1 - \sqrt {x}}{1 + \sqrt {x}} ~dx = \color{blue} {- x + 4 \sqrt {x} - 4 \ln (1 + x)}$

- **Solution:** $u = 1 + \sqrt {x}$, $x = (u - 1)^2$, $dx = 2(u - 1) ~du$

- **Solution:** $\frac {1 - \sqrt {x}}{1 + \sqrt {x}} ~dx = \frac {2 - u}{u} 2(u - 1) ~du = -2u + 6 - 4 \cdot \frac {1}{u} ~du$

- **Used 2019**, *Unsolved*

2. $\displaystyle \int \frac {1}{\sqrt {x}+2\sqrt[3]{x}} ~dx = \color {blue} {2\sqrt {x} - 6\sqrt[3]{x} + 24\sqrt[6]{x} - 48\ln (\sqrt[6]{x} + 2)}$

- **Solution:** $u_1^6 = x$, $6 u_1^5 ~du_1 = dx$

- **Solution:** $u_2 = u_1 + 2$, $du_2 = du_1$

- **Solution:** $\frac {1}{\sqrt {x}+2\sqrt[3]{x}} ~dx = \frac {1}{u_1^3 + 2 u_1^2} \cdot 6u_1^5 ~du_1 = \frac {6u_1^3}{u_1 + 2} ~du_1 = \frac {6(u_2 - 2)^3}{u_2} ~du_2 = 6 (u_2^2 - 6u_2 + 12 - 8 \cdot \frac {1}{u_2}) ~du_2$

3. $\displaystyle \int \frac {1}{\sqrt {x} - \sqrt[3]{x}} ~dx ＝ \color {blue} {2\sqrt {x}+3\sqrt[3]{x}+6\sqrt[6]{x}+6\ln (\sqrt[6]{x} - 1)}$

- **Solution:** $u_1^6 = x$, $6 u_1^5 ~du_1 = dx$

- **Solution:** $u_2 = u_1 - 1$, $du_2 = du_1$

- **Solution: ** $\frac {1}{\sqrt {x} - \sqrt[3]{x}} ~dx = \frac {1}{u_1^3 - u_1^2} \cdot 6 u_1^5 ~du_1 = \frac {6u_1^3}{u_1 - 1} ~du_1 = \frac {6(u_2 + 1)^3}{u_2} ~du_2 = 6 (u_2^2 + 3u_2 + 3 + \cdot \frac {1}{u_2}) ~du_2$

- **Used 2019**, *Unosolved*

4. $\displaystyle \int \frac {1}{\sqrt {x} + \sqrt[4]{x}} ~dx = \color {blue} {2\sqrt {x}-4\sqrt[4]{x}+4\ln(\sqrt[4]{x}+1)}$

- **Solution:** $u_1^4 = x$, $4 u_1^3 ~du_1 = dx$

- **Solution:** $u_2 = u_1 + 1$, $du_2 = du_1$

- **Solution:** $\frac {1}{\sqrt {x} + \sqrt[4]{x}} ~dx = \frac {1}{u_1^2 + u_1} \cdot 4 u_1^3 ~du_1 = \frac {4 u_1^2}{u_1 + 1} ~du_1 = \frac {4 (u_2 - 1)^2}{u_2} ~du_2 = 4(u_2 - 2 + \frac {1}{u_2}) ~du_2$

5. $\displaystyle \int \frac {\sqrt[3]{x}+1}{\sqrt[3]{x} - 1} ~dx = \color {blue} {x+3\sqrt[3]{x}^2+6\sqrt[3]{x}+6\ln(\sqrt[3]{x} - 1)}$

- **Solution:** $u_1^3 = x$, $3 u_1^2 ~du_1 = dx$

- **Solution:** $u_2 = u_1 - 1$, $du_2 = du_1$

- **Solution:** $\frac {\sqrt[3]{x}+1}{\sqrt[3]{x} - 1} ~dx = \frac {u_1 + 1}{u_1 - 1} \cdot 3 u_1^2 ~du_1 = \frac {3(u_2 + 2)(u_2 + 1)^2}{u_2} ~du_2 = 3(u_2^2 + 4u_2 + 5 + 2 \cdot \frac {1}{u_2}) ~du_2$

- **Used 2019**

6. $\displaystyle \int \frac {1}{(x+1)\sqrt {x}} ~dx = \color{blue} {2 \tan ^{-1} (\sqrt {x})}$

- **Solution:** $u = \sqrt {x}​$, $du = \frac {1}{2 \sqrt {x}} ~dx​$

- **Solution:** $\frac {1}{(x+1)\sqrt {x}} ~dx = \frac {2}{u^2 + 1} ~du​$

  1. $\displaystyle \int \frac {1}{2x\sqrt {x-1}} ~dx =  \color{blue} {\tan^{-1}(\sqrt {x-1})}​$

  - **Solution:** $\frac {1}{2x \sqrt {x-1}} = \frac {1}{2(x - 1 + 1) \sqrt {x-1}}$

7. $\displaystyle \int \frac {x}{\sqrt[3]{x + 1}} ~dx = \color {blue} {\frac {3}{5} (x + 1)^{\frac {5}{3}} - \frac {3}{2} (x + 1)^{\frac {2}{3}}}​$

- **Solution:** $u = x + 1$, $du = dx$

- **Solution:** $\frac {x}{\sqrt[3]{x + 1}} ~dx = \frac {u - 1}{\sqrt[3]{u}} ~du = u^{\frac {2}{3}} - u^{- \frac {1}{3}} ~du$

- **Used 2019**

8. $\displaystyle \int \frac {1}{x\sqrt {4x-1}} ~dx = \color{blue} {2 \tan ^{-1} (\sqrt {4x - 1})}​$

- **Solution:** $u = \sqrt {4x-1}​$, $x = \frac {1}{4} (u^2 + 1)​$, $dx = \frac {1}{2} u ~du​$

- **Solution:** $\frac {1}{x\sqrt {4x-1}} ~dx = \frac {2}{u^2 + 1} ~du​$

9. $\displaystyle \int \frac {2}{x\sqrt {25x^4-1}} ~dx = \color{blue} {\tan^{-1}(\sqrt {25x^4-1})}​$

- **Solution:** $u = \sqrt {25x^4 - 1}​$, $x^4 = \frac {1}{25} (u^2 + 1)​$, $4x^3 ~dx = \frac {2}{25} u ~du​$

- **Solution:** $\frac {2}{x\sqrt {25x^4-1}} ~dx = \frac {1}{u^2 + 1} ~du$

10. $\displaystyle \int \frac {1}{\sqrt {x}\sqrt {1-4x}} ~dx = \color{blue} {\frac {1}{2} \sin ^{-1} (8x - 1)} = \color{blue} {\sin ^{-1} (2\sqrt {x})}$

- **Solution:** $u = 8x - 1$, $du = 8 ~dx$

- **Solution:** $\frac {1}{\sqrt {x}\sqrt {1-4x}} ~dx = \frac {1}{\sqrt {1 - (8x - 1)^2}} ~dx = \frac {1}{2} \cdot \frac {1}{\sqrt {1 - u^2}} ~du​$

- **Another Solution:** $u = 2 \sqrt {x}$, $du = \frac {1}{\sqrt {x}} ~dx$

- **Another Solution:** $\frac {1}{\sqrt {x}\sqrt {1-4x}} ~dx = \frac {1}{\sqrt {1 - u^2}} ~du​$

11. $\displaystyle \int \frac {6-2x}{\sqrt {9-x^2}} ~dx = \color {blue} {6 \sin ^{-1} (\frac {x}{3}) + 2 \sqrt {9-x^2}}$

- **Solution:** $u = \frac {1}{3} x​$, $du = \frac {1}{3} ~dx​$

- **Solution:** $\frac {6-2x}{\sqrt {9-x^2}} ~dx = \frac {6}{\sqrt {1-u^2}} ~du + \frac {- 2x}{\sqrt {9-x^2}} ~dx$

12. $\displaystyle \int \frac {1}{\sqrt {x\sqrt {x}-x^2}} ~dx = \color {blue} {4 \sin ^{-1} (\sqrt[4]{x})}$

- **Solution:** $u = \sqrt[4]{x}$, $du = \frac {1}{4 \sqrt[4]{x^3}} ~dx$

- **Solution:** $\frac {1}{\sqrt {x\sqrt {x}-x^2}} ~dx = \frac {1}{\sqrt {1 - (\sqrt[4]{x})^2}} \cdot \frac {1}{4 \sqrt[4]{x^3}} ~dx = 4 \frac {1}{\sqrt {1 - u^2}} ~du$

- **Used 2019**, *Unsolved*
