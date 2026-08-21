---
schema: qual/card@1
id: P-NHFXM
kind: problem
title: Antiderivatives of $\frac{1}{\sin x+\cos x}$ and $\frac{\sin x}{1\pm\sin x}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
solved: false
---

::: problem
1. $\displaystyle \int \frac {1}{\sin (x) + \cos (x)} ~dx = \color {blue}{\frac {1}{\sqrt {2}} (\ln (\tan (\frac {x}{2}) - 1 + \sqrt {2}) - \ln (\tan (\frac {x}{2}) - 1 - \sqrt {2}))} = \color {blue} {- \frac {1}{\sqrt {2}} \ln (\csc (x + \frac {\pi}{4}) - \cot (x + \frac {\pi}{4}))}$

- **Solution:** $\frac {1}{\sin (x) + \cos (x)} ~dx = \frac {1}{\frac {2u}{1 + u^2} + \frac {1 - u^2}{1 + u^2}} \cdot  \frac {2}{1 + u^2} ~du = \frac {1 + u^2}{2u + 1 - u^2} \cdot  \frac {2}{1 + u^2} ~du = \frac {1}{\sqrt {2}} (\frac {1}{u + \sqrt {2} - 1} - \frac {1}{u - \sqrt {2} - 1}) ~du​$

- **Another Solution:** $\frac {1}{\sin (x) + \cos (x)} ~dx = \frac {1}{\sqrt {2} \sin (x + \frac {\pi}{4})} ~dx = \frac {1}{\sqrt {2}} \csc (x + \frac {\pi}{4}) ~dx$

- $\ln (\csc (x + \frac {\pi}{4}) - \cot (x + \frac {\pi}{4}))​$

- $= \frac {1 - \cos (x + \frac {\pi}{4})}{\sin (x + \frac {\pi}{4})} = \frac {1 - \frac {1}{\sqrt {2}} (- \sin (x) + \cos (x))}{\frac {1}{\sqrt {2}} (\sin (x) + \cos (x))} = \frac {1 + \frac {1}{\sqrt {2}} (\frac {2 \tan (\frac {x}{2})}{1 + \tan ^2 (\frac {x}{2})} - \frac {1 - \tan ^2 (\frac {x}{2})}{1 + \tan ^2 (\frac {x}{2})})}{\frac {1}{\sqrt {2}} (\frac {2 \tan (\frac {x}{2})}{1 + \tan ^2 (\frac {x}{2})} + \frac {1 - \tan ^2 (\frac {x}{2})}{1 + \tan ^2 (\frac {x}{2})})}$

- $= \frac {1 + \tan ^2 (\frac {x}{2}) + \frac {1}{\sqrt {2}} (2 \tan (\frac {x}{2}) - 1 + \tan ^2 (\frac {x}{2}))}{\frac {1}{\sqrt {2}} (2 \tan (\frac {x}{2}) + 1 - \tan ^2 (\frac {x}{2}))} = \frac {(\frac {1}{\sqrt {2}} + 1) \tan ^2 (\frac {x}{2}) + \sqrt {2} \tan (\frac {x}{2}) + (- \frac {1}{\sqrt {2}} + 1)}{- \frac {1}{\sqrt {2}} ((\tan (\frac {x}{2}) - 1)^2 - 2)} = - \frac {(\sqrt {2} + 1) (\tan (\frac {x}{2}) -1 + \sqrt {2})^2}{(\tan (\frac {x}{2}) - 1 + \sqrt {2})(\tan (\frac {x}{2}) - 1 - \sqrt {2})}​$

- $= - (\sqrt {2} + 1) \frac {\tan (\frac {x}{2}) - 1 + \sqrt {2}}{\tan (\frac {x}{2}) - 1 - \sqrt {2}}​$

2. $\displaystyle \int \frac {\sin(x)}{1 + \sin(x)} ~dx = 2(\tan ^{-1} (\tan (\frac {x}{2})) + \frac {1}{\tan (\frac {x}{2}) + 1}) = \color {blue} {x + \frac {2}{\tan (\frac {x}{2}) + 1}}= \color {blue} {x + \frac {2\sin(\frac {x}{2})}{\sin(\frac {x}{2}) + \cos(\frac {x}{2})}} = \color {blue} {x + \sec (x) - \tan (x)}$

- **Solution:** $\frac {\sin(x)}{1 + \sin(x)} ~dx = \frac {\frac {2u}{1 + u^2}}{1 + \frac {2u}{1 + u^2}} \cdot \frac {2}{1 + u^2} ~du = \frac {2u}{1 + u^2 + 2u} \cdot \frac {2}{1 + u^2} ~du = 2(\frac {1}{1 + u^2} - \frac {1}{(u + 1)^2}) ~du​$

  1. $\displaystyle \int \frac {1}{1+\sin (x)} ~dx = \color {blue} {- \frac {2}{\tan (\frac {x}{2}) + 1}} $

  - **Solution:** $\frac {1}{1 + \sin(x)} = 1 - \frac {\sin(x)}{1 + \sin(x)}$

  2. $\displaystyle \int \frac {\tan(x)}{\tan(x) + \sec(x)} ~dx =\color {blue} {x + \frac {2}{\tan (\frac {x}{2}) + 1}}​$

  - **Solution:** $\frac {\tan(x)}{\tan(x) + \sec(x)} = \frac {\sin (x)}{1 + \sin (x)}$

  - **Used 2019**, *Unsolved*

3. $\displaystyle \int \frac {\sin (x)}{1-\sin(x)} ~dx = 2(- \frac {1}{\tan (\frac {x}{2}) - 1} - \tan ^{-1} (\tan (\frac {x}{2}))) = \color {blue} {- \frac {2}{\tan (\frac {x}{2}) - 1} - x} = \color {blue} {- \frac {2\sin(\frac {x}{2})}{\cos(\frac {x}{2}) -\sin(\frac {x}{2})} - x}$

- **Solution:** $\frac {\sin(x)}{1 - \sin(x)} ~dx = \frac {\frac {2u}{1 + u^2}}{1 - \frac {2u}{1 + u^2}} \cdot \frac {2}{1 + u^2} ~du = \frac {2u}{1 + u^2 - 2u} \cdot \frac {2}{1 + u^2} ~du = 2(\frac {1}{(u - 1)^2} - \frac {1}{1 + u^2}) ~du$
:::
