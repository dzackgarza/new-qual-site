---
schema: qual/card@1
id: P-F6K7Y
kind: problem
title: "1. $\\displaystyle \\int \\sec^3(x) ~dx = \\color {blue} {\\frac {1}{2} (\\l\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

1. $\displaystyle \int \sec^3(x) ~dx = \color {blue} {\frac {1}{2} (\ln (\sec (x) + \tan (x)) + \tan (x) \sec (x))} = \color {blue} {\frac {1}{2} (\ln(\frac {\cos(\frac {x}{2}) +\sin(\frac {x}{2})}{\cos(\frac {x}{2}) -\sin(\frac {x}{2})}) + \tan (x) \sec (x))}$

- **Solution:** $\frac {3 - 2}{3 - 1} \int \sec ^{3 - 2} (x) ~dx + \frac {1}{3 - 1} \tan (x) \sec ^{3 - 2} (x) = \frac {1}{2}  \int \sec (x) ~dx + \frac {1}{2} \tan (x) \sec (x)$

2. $\displaystyle \int \sec^4(x) ~dx = \color {blue} {\frac {2}{3} \tan (x) + \frac {1}{3} \tan (x) \sec ^2 (x)} = \color {blue} {\frac {1}{3} \tan ^3 (x) + \tan (x)}$

- **Solution:** $\frac {4 - 2}{4 - 1} \int \sec ^{4 - 2} (x) ~dx + \frac {1}{4 - 1} \tan (x) \sec ^{4 - 2} (x) = \frac {2}{3} \int \sec ^2 (x) ~dx + \frac {1}{3} \tan (x) \sec ^2 (x)$

  1. $\displaystyle \int \frac {1}{\cos^4(x)} ~dx = \color {blue} {\frac {2}{3} \tan (x) + \frac {1}{3} \tan (x) \sec ^2 (x)} = \color {blue} {\frac {1}{3} \tan ^3 (x) + \tan (x)}$

  - **Solution:** $\frac {1}{\cos^4(x)} = \sec ^4 (x)$

3. $\displaystyle \int \tan ^2 (x) ~dx = \color {blue} {\tan (x) - x}$

- **Solution:** $\tan ^2 (x) = \sec ^2 (x) - 1$

4. $\displaystyle \int \tan ^3 (x) ~dx = \color {blue} {\frac {1}{2} \tan ^2 (x) + \ln (\cos (x))} = \color {blue} {\frac {1}{2} \sec^2 (x) - \ln (\sec (x))}$

- **Solution:** $\tan ^3 (x) = (\sec ^2 (x) - 1) \tan (x)$

- **Another Solution:** $u = \sec (x)$, $du = \sec (x) \tan (x) ~dx$

- **Another Solution:** $\tan ^3 (x) ~dx = (\sec ^2 (x) - 1) \tan (x) ~dx = \frac {u^2 - 1}{u} ~du = (u - \frac {1}{u}) ~du$

5. $\displaystyle \int \tan ^4 (x) ~dx = \color {blue} {\frac {1}{3} \tan ^3 (x) - \tan (x) + x}$

- **Solution:** $\tan ^4 (x) = (\sec ^2 (x) - 1) \tan ^2 (x) = \sec ^2 (x) \tan ^2 (x) - (\sec ^2 (x) - 1)$

6. $\displaystyle \int \sec^3(x)\tan^3(x) ~dx = \color {blue} {-\frac {1}{3} \sec ^3(x) + \frac {1}{5} \sec ^5(x)}$

- **Solution:** $ \sec^3(x)\tan^3(x) ~dx =  \sec ^2 (x) (\sec ^2 (x) - 1) \sec (x) \tan (x) ~dx = \sec ^4 (x) - \sec ^2 (x)) ~d \sec (x)$

7. $\displaystyle \int \tan^4(x) + \tan^2(x) ~dx = \color {blue} {\frac {1}{3} \tan^3(x)}$

- **Solution:** $\tan^4(x) + \tan^2(x) ~dx = \tan ^2 (x) (\tan^2(x) + 1) ~dx = \tan ^2 (x) \sec ^2 (x) ~dx = \tan ^2 (x) ~d \tan (x)$

8. $\displaystyle \int \frac {2\sin^2 (x)}{\cos^3 (x)} ~dx = \color {blue} {- \ln(\tan (x) + \sec (x)) + \tan (x) \sec (x)} = \color {blue} {\ln(\sec (x) - \tan (x)) + \tan (x) \sec (x)} = \tan (x) \sec (x) - \frac {1}{2}(\ln (\sin (x)+1) - \ln (\sin (x)-1))???$

- **Solution:** $\frac {2\sin^2 (x)}{\cos^3 (x)} = 2 \tan^2 (x) \sec (x) = 2 (\sec^2 (x) - 1) \sec (x) = 2(\sec^3 (x) -\sec (x))$
