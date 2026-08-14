---
schema: qual/card@1
id: P-PV5GI
kind: problem
title: "$\\displaystyle \\int \\frac {\\sqrt {1 + \\ln (x)}}{x \\ln (x)} ~dx = \\color {blue} {2 \\sqrt {1 + \\ln (x)} + \\ln (\\sqrt {1 + \\ln (x)} - 1) - \\ln (\\sqrt {1 + \\ln (x)} + 1)}$ Solution: $u = \\sqrt {1 + \\ln (x)}$\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
relations: []
review: draft
---

3. $\displaystyle \int \frac {\sqrt {1 + \ln (x)}}{x \ln (x)} ~dx = \color {blue} {2 \sqrt {1 + \ln (x)} + \ln (\sqrt {1 + \ln (x)} - 1) - \ln (\sqrt {1 + \ln (x)} + 1)}$

- **Solution:** $u = \sqrt {1 + \ln (x)}$, $x = e^{u^2 - 1}$, $dx = 2u e^{u^2 - 1} ~du$

- **Solution:** $\frac {\sqrt {1 + \ln (x)}}{x \ln (x)} ~dx = \frac {u}{e^{u^2 - 1} {u^2 - 1}} \cdot 2u e^{u^2 - 1} ~du = \frac {2u^2}{u^2 - 1} ~du = 2 + \frac {1}{u - 1} - \frac {1}{u + 1} ~du$

4. $\displaystyle \int \frac {7 - \ln (x)}{x(3 + \ln (x))} ~dx = \color{blue} {- \ln (x) + 10 \ln (\ln (x) + 3)}$

- **Solution: ** $u = \ln (x) + 3$, $du = \frac {1}{x} ~dx$

- **Solution:** $\frac {7 - \ln (x)}{x(3 + \ln (x))} ~dx = - \frac {dx}{x} + 10 \frac {\frac {1}{x} ~dx}{3 + \ln (x)} = - \frac {dx}{x} + 10 \frac {du}{u}$

5. $\displaystyle \int \frac {\sec^2(x)}{1+\tan(x)} ~dx = \color {blue} {\ln (\tan (x) + 1)}$

- **Solution:** $u = 1 + \tan (x)$, $du = \sec ^2 (x) ~dx$

6. $\displaystyle \int \frac {\sin(x)}{\sqrt {4-\cos^2(x)}} ~dx = \color {blue} {- \sin^{-1}(\frac {1}{2} \cos(x))}$

- **Solution:** $u = \frac {1}{2} \cos (x)$, $du = - \frac {1}{2} \sin (x) ~ dx$

- **Solution:** $\frac {\sin(x)}{\sqrt {4-\cos^2(x)}} ~dx = - \frac {1}{\sqrt {1 - u^2}} ~du$

7. $\displaystyle \int \frac {\sec ^2 (x)}{\sqrt {9 - \tan^2(x)}} ~dx = \color {blue} {- \sin^{-1}(\frac {1}{3} \tan(x))}$

- **Solution:** $u = \frac {1}{3} \tan (x)$, $du = - \frac {1}{3} \sec ^2 (x) ~ dx$

- **Solution:** $\frac {\sec ^2 (x)}{\sqrt {9 - \tan^2(x)}} ~dx = - \frac {1}{\sqrt {1 - u^2}} ~du$
