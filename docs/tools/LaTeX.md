# LaTeX 备忘清单

本备忘单总结了 [LaTeX](https://www.latex-project.org/) 常用显示数学符号的参考列表和一些 [KaTeX](https://katex.org/) 的应用示例。

## 入门

### 介绍

[LaTeX](https://www.latex-project.org/) 基于 TEX 的排版系统，适用于生成高印刷质量的科技和数学、物理文档。

- [LaTeX 官网](https://www.latex-project.org/) _(latex-project.org)_

而 [KaTeX](https://katex.org/) 只处理 LaTeX 的数学符号的一个更小的子集，用于 web 上展示

- [KaTeX 官网](https://katex.org/) _(katex.org)_

### 示例

```KaTeX
% \f is defined as #1f(#2) using the macro
f\relax(x) = \int_{-\infty}^\infty
    f\hat\xi\,e^{2 \pi i \xi x}
    \,\mathrm{d}\xi
```

```LaTeX
% \f is defined as #1f(#2) using the macro
f\relax(x) = \int_{-\infty}^\infty
    f\hat\xi\,e^{2 \pi i \xi x}
    \,\mathrm{d}\xi
```

### 行内展示

```markdown
基于 KaTeX 在一行
展示示例： `KaTeX:\int_0^\infty x^2 dx`
```

基于 KaTeX 在一行展示示例： `KaTeX:\int_0^\infty x^2 dx`

## 支持的语法

### 标注符号

| :- | :- | :- |
| :- | :- | :- |
| `KaTeX:a'` `a'` | `KaTeX:\tilde{a}` `\tilde{a}` | `KaTeX:\mathring{g}` `\mathring{g}` |
| `KaTeX:a''` `a''` | `KaTeX:\widetilde{ac}` `\widetilde{ac}` | `KaTeX:\overgroup{AB}` `\overgroup{AB}` |
| `KaTeX:a^{\prime}` `a^{\prime}` | `KaTeX:\utilde{AB}` `\utilde{AB}` | `KaTeX:\undergroup{AB}` `\undergroup{AB}` |
| `KaTeX:\acute{a}` `\acute{a}` | `KaTeX:\vec{F}` `\vec{F}` | `KaTeX:\Overrightarrow{AB}` `\Overrightarrow{AB}` |
| `KaTeX:\bar{y}` `\bar{y}` | `KaTeX:\overleftarrow{AB}` `\overleftarrow{AB}` | `KaTeX:\overrightarrow{AB}` `\overrightarrow{AB}` |
| `KaTeX:\breve{a}` `\breve{a}` | `KaTeX:\underleftarrow{AB}` `\underleftarrow{AB}` | `KaTeX:\underrightarrow{AB}` `\underrightarrow{AB}` |
| `KaTeX:\check{a}` `\check{a}` | `KaTeX:\overleftharpoon{ac}` `\overleftharpoon{ac}` | `KaTeX:\overrightharpoon{ac}` `\overrightharpoon{ac}` |
| `KaTeX:\dot{a}` `\dot{a}` | `KaTeX:\overleftrightarrow{AB}` `\overleftrightarrow{AB}` | `KaTeX:\overbrace{AB}` `\overbrace{AB}` |
| `KaTeX:\ddot{a}` `\ddot{a}` | `KaTeX:\underleftrightarrow{AB}` `\underleftrightarrow{AB}` | `KaTeX:\underbrace{AB}` `\underbrace{AB}` |
| `KaTeX:\grave{a}` `\grave{a}` | `KaTeX:\overline{AB}` `\overline{AB}` | `KaTeX:\overlinesegment{AB}` `\overlinesegment{AB}` |
| `KaTeX:\hat{\theta}` `\hat{\theta}` | `KaTeX:\underline{AB}` `\underline{AB}` | `KaTeX:\underlinesegment{AB}` `\underlinesegment{AB}` |
| `KaTeX:\widehat{ac}` `\widehat{ac}` | `KaTeX:\widecheck{ac}` `\widecheck{ac}` | `KaTeX:\underbar{X}` `\underbar{X}` |

### \text｛…｝中的强调功能

| :- | :- | :- |
| :- | :- | :- |
| `KaTeX:\'{a}` `\'{a}` | `KaTeX:\~{a}` `\~{a}` |
| `KaTeX:\.{a}` `\.{a}` | `KaTeX:\H{a}` `\H{a}` |
| ``KaTeX:\\\`{a}`` ``\`{a}`` | `KaTeX:\={a}` `\={a}` |
| `KaTeX:\"{a}` `\"{a}` | `KaTeX:\v{a}` `\v{a}` |
| `KaTeX:\^{a}` `\^{a}` | `KaTeX:\u{a}` `\u{a}` |
| `KaTeX:\r{a}` `\r{a}` |

### 定界符大小调整

| :- | :- |
| :- | :- |
| `KaTeX:\left(\LARGE{AB}\right)` | `\left(\LARGE{AB}\right)` |
| `KaTeX:( \big( \Big( \bigg( \Bigg(` | `( \big( \Big( \bigg( \Bigg(` |

| :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- |
| `\left` | `\big` | `\bigl` | `\bigm` | `\bigr` |
| `\middle` | `\Big` | `\Bigl` | `\Bigm` | `\Bigr` |
| `\right` | `\bigg` | `\biggl` | `\biggm` | `\biggr` |
| `\` | `\Bigg` | `\Biggl` | `\Biggm` | `\Biggr` |

### 希腊和希伯来字母

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\alpha` | `\alpha` | `KaTex:\kappa` | `\kappa` | `KaTex:\psi` | `\psi` | `KaTex:\digamma` | `\digamma` | `KaTex:\Delta` | `\Delta` | `KaTex:\Theta` | `\Theta` |
| `KaTex:\beta` | `\beta` | `KaTex:\lambda` | `\lambda` | `KaTex:\rho` | `\rho` | `KaTex:\varepsilon` | `\varepsilon` | `KaTex:\Gamma` | `\Gamma` | `KaTex:\Upsilon` | `\Upsilon` |
| `KaTex:\chi` | `\chi` | `KaTex:\mu` | `\mu` | `KaTex:\sigma` | `\sigma` | `KaTex:\varkappa` | `\varkappa` | `KaTex:\Lambda` | `\Lambda` | `KaTex:\Xi` | `\Xi` |
| `KaTex:\delta` | `\delta` | `KaTex:\nu` | `\nu` | `KaTex:\tau` | `\tau` | `KaTex:\varphi` | `\varphi` | `KaTex:\Omega` | `\Omega` |  |
| `KaTex:\epsilon` | `\epsilon` | `KaTex:o` | `o` | `KaTex:\theta` | `\theta` | `KaTex:\varpi` | `\varpi` | `KaTex:\Phi` | `\Phi` | `KaTex:\aleph` | `\aleph` |
| `KaTex:\eta` | `\eta` | `KaTex:\omega` | `\omega` | `KaTex:\upsilon` | `\upsilon` | `KaTex:\varrho` | `\varrho` | `KaTex:\Pi` | `\Pi` | `KaTex:\beth` | `\beth` |
| `KaTex:\gamma` | `\gamma` | `KaTex:\phi` | `\phi` | `KaTex:\xi` | `\xi` | `KaTex:\varsigma` | `\varsigma` | `KaTex:\Psi` | `\Psi` | `KaTex:\daleth` | `\daleth` |
| `KaTex:\iota` | `\iota` | `KaTex:\pi` | `\pi` | `KaTex:\zeta` | `\zeta` | `KaTex:\vartheta` | `\vartheta` | `KaTex:\Sigma` | `\Sigma` | `KaTex:\gimel` | `\gimel` |

其它字母

| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\imath` | `\imath` | `KaTex:\nabla` | `\nabla` | `KaTex:\Im` | `\Im` | `KaTex:\Reals` | `\Reals` | `KaTex:\text{\OE}` | `\text{\OE}` |
| `KaTex:\jmath` | `\jmath` | `KaTex:\partial` | `\partial` | `KaTex:\image` | `\image` | `KaTex:\wp` | `\wp` | `KaTex:\text{\o}` | `\text{\o}` |
| `KaTex:\aleph` | `\aleph` | `KaTex:\Game` | `\Game` | `KaTex:\Bbbk` | `\Bbbk` | `KaTex:\weierp` | `\weierp` | `KaTex:\text{\O}` | `\text{\O}` |
| `KaTex:\alef` | `\alef` | `KaTex:\Finv` | `\Finv` | `KaTex:\N` | `\N` | `KaTex:\Z` | `\Z` | `KaTex:\text{\ss}` | `\text{\ss}` |
| `KaTex:\alefsym` | `\alefsym` | `KaTex:\cnums` | `\cnums` | `KaTex:\natnums` | `\natnums` | `KaTex:\text{\aa}` | `\text{\aa}` | `KaTex:\text{\i}` | `\text{\i}` |
| `KaTex:\beth` | `\beth` | `KaTex:\Complex` | `\Complex` | `KaTex:\R` | `\R` | `KaTex:\text{\AA}` | `\text{\AA}` | `KaTex:\text{\j}` | `\text{\j}` |
| `KaTex:\gimel` | `\gimel` | `KaTex:\ell` | `\ell` | `KaTex:\Re` | `\Re` | `KaTex:\text{\ae}` | `\text{\ae}` |
| `KaTex:\daleth` | `\daleth` | `KaTex:\hbar` | `\hbar` | `KaTex:\real` | `\real` | `KaTex:\text{\AE}` | `\text{\AE}` |
| `KaTex:\eth` | `\eth` | `KaTex:\hslash` | `\hslash` | `KaTex:\reals` | `\reals` | `KaTex:\text{\oe}` | `\text{\oe}` |

### 字母和 Unicode

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\Alpha` | `\Alpha` | `KaTex:\Beta` | `\Beta` | `KaTex:\Gamma` | `\Gamma` | `KaTex:\Delta` | `\Delta` |
| `KaTex:\Epsilon` | `\Epsilon` | `KaTex:\Zeta` | `\Zeta` | `KaTex:\Eta` | `\Eta` | `KaTex:\Theta` | `\Theta` |
| `KaTex:\Iota` | `\Iota` | `KaTex:\Kappa` | `\Kappa` | `KaTex:\Lambda` | `\Lambda` | `KaTex:\Mu` | `\Mu` |
| `KaTex:\Nu` | `\Nu` | `KaTex:\Xi` | `\Xi` | `KaTex:\Omicron` | `\Omicron` | `KaTex:\Pi` | `\Pi` |
| `KaTex:\Rho` | `\Rho` | `KaTex:\Sigma` | `\Sigma` | `KaTex:\Tau` | `\Tau` | `KaTex:\Upsilon` | `\Upsilon` |
| `KaTex:\Phi` | `\Phi` | `KaTex:\Chi` | `\Chi` | `KaTex:\Psi` | `\Psi` | `KaTex:\Omega` | `\Omega` |
| `KaTex:\varGamma` | `\varGamma` | `KaTex:\varDelta` | `\varDelta` | `KaTex:\varTheta` | `\varTheta` | `KaTex:\varLambda` | `\varLambda` |
| `KaTex:\varXi` | `\varXi` | `KaTex:\varPi` | `\varPi` | `KaTex:\varSigma` | `\varSigma` | `KaTex:\varUpsilon` | `\varUpsilon` |
| `KaTex:\varPhi` | `\varPhi` | `KaTex:\varPsi` | `\varPsi` | `KaTex:\varOmega` | `\varOmega` |
| `KaTex:\alpha` | `\alpha` | `KaTex:\beta` | `\beta` | `KaTex:\gamma` | `\gamma` | `KaTex:\delta` | `\delta` |
| `KaTex:\epsilon` | `\epsilon` | `KaTex:\zeta` | `\zeta` | `KaTex:\eta` | `\eta` | `KaTex:\theta` | `\theta` |
| `KaTex:\iota` | `\iota` | `KaTex:\kappa` | `\kappa` | `KaTex:\lambda` | `\lambda` | `KaTex:\mu` | `\mu` |
| `KaTex:\nu` | `\nu` | `KaTex:\xi` | `\xi` | `KaTex:\omicron` | `\omicron` | `KaTex:\pi` | `\pi` |
| `KaTex:\rho` | `\rho` | `KaTex:\sigma` | `\sigma` | `KaTex:\tau` | `\tau` | `KaTex:\upsilon` | `\upsilon` |
| `KaTex:\phi` | `\phi` | `KaTex:\chi` | `\chi` | `KaTex:\psi` | `\psi` | `KaTex:\omega` | `\omega` |
| `KaTex:\varepsilon` | `\varepsilon` | `KaTex:\varkappa` | `\varkappa` | `KaTex:\vartheta` | `\vartheta` | `KaTex:\thetasym` | `\thetasym` |
| `KaTex:\varpi` | `\varpi` | `KaTex:\varrho` | `\varrho` | `KaTex:\varsigma` | `\varsigma` | `KaTex:\varphi` | `\varphi` |
| `KaTex:\digamma` | `\digamma` |

### 注解

| :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- |
| `KaTex:\cancel{5}` | `\cancel{5}` | `KaTex:\overbrace{a+b+c}^{\text{note}}` | `\overbrace{a+b+c}^{\text{note}}` |
| `KaTex:\bcancel{5}` | `\bcancel{5}` | `KaTex:\underbrace{a+b+c}_{\text{note}}` | `\underbrace{a+b+c}_{\text{note}}` |
| `KaTex:\xcancel{ABC}` | `\xcancel{ABC}` | `KaTex:\not =` | `\not =` |
| `KaTex:\sout{abc}` | `\sout{abc}` | `KaTex:\boxed{\pi=\frac c d}` | `\boxed{\pi=\frac c d}` |
| `KaTex:\$a_{\angl n}` _MD语法冲突_ | `$a_{\angl n}` | `KaTex:a_\angln` | `a_\angln` |
| `KaTex:\phase{-78^\circ}` | `\phase{-78^\circ}` |

\tag{hi} x+y^{2x}

```KaTex
\tag{hi} x+y^{2x}
```

\tag*{hi} x+y^{2x}

```KaTex
\tag*{hi} x+y^{2x}
```

### 垂直布局

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTex:x_n` | `x_n` | `KaTex:\stackrel{!}{=}` | `\stackrel{!}{=}` | `KaTex:a \atop b` | `a \atop b` |
| `KaTex:e^x` | `e^x` | `KaTex:\overset{!}{=}` | `\overset{!}{=}` | `KaTex:a\raisebox{0.25em}{$b$}c` | `a\raisebox{0.25em}{$b$}c` |
| `KaTex:_u^o` | `_u^o` | `KaTex:\underset{!}{=}` | `\underset{!}{=}` | `KaTex:a+\left(\vcenter{\hbox{$\frac{\frac a b}c$}}\right)` | `a+\left(\vcenter{\hbox{$\frac{\frac a b}c$}}\right)` |
| `KaTex:\sum_{\substack{0<i<m\\0<j<n}}` | `\sum_{\substack{0<i<m\\0<j<n}}` |

### 重叠和间距

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTex:{=}\mathllap{/\,}` {=}\mathllap{/\,} | `KaTex:\left(x^{\smash{2}}\right)` | \left(x^{\smash{2}}\right) |
| `KaTex:\mathrlap{\,/}{=}` \mathrlap{\,/}{=} | `KaTex:\sqrt{\smash[b]{y}}` | \sqrt{\smash[b]{y}} |

`\sum_{\mathclap{1\le i\le j\le n}} x_{ij}`

```KaTex
\sum_{\mathclap{1\le i\le j\le n}} x_{ij}
```

### `KaTex:\LaTeX` 数学结构

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- |
| `KaTex:\frac{abc}{xyz}` | `\frac{abc}{xyz}` | `KaTex:\overline{abc}` | `\overline{abc}` | `KaTex:\overrightarrow{abc}` | `\overrightarrow{abc}` |
| `KaTex:f'` | `f'` | `KaTex:\underline{abc}` | `\underline{abc}` | `KaTex:\overleftarrow{abc}` | `\overleftarrow{abc}` |
| `KaTex:\sqrt{abc}` | `\sqrt{abc}` | `KaTex:\widehat{abc}` | `\widehat{abc}` | `KaTex:\overbrace{abc}` | `\overbrace{abc}` |
| `KaTex:\sqrt[n]{abc}` | `\sqrt[n]{abc}` | `KaTex:\widetilde{abc}` | `\widetilde{abc}` | `KaTex:\underbrace{abc}` | `\underbrace{abc}` |

### 分隔符

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTeX:()` | `()` | `KaTeX:\lparen \rparen` | `\lparen` `\rparen` | `KaTex:⌈ ⌉` | `⌈ ⌉` | `KaTex:\lceil \rceil` | `\lceil` `\rceil` | `KaTex:\uparrow` | `\uparrow` |
| `KaTeX:[]` | `[]` | `KaTeX:\lbrack \rbrack` | `\lbrack` `\rbrack` | `KaTex:⌊ ⌋` | `⌊ ⌋` | `KaTex:\lfloor \rfloor` | `\lfloor` `\rfloor` | `KaTex:\downarrow` | `\downarrow` |
| `KaTeX:\{ \}` | `{}` | `KaTex:\lbrace \rbrace` | `\lbrace` `\rbrace` | `KaTex:⎰⎱` | `⎰⎱` | `KaTex:\lmoustache  \rmoustache` | `\lmoustache` `\rmoustache` | `KaTex:\updownarrow` | `\updownarrow` |
| `KaTeX:⟨ ⟩` | `⟨⟩` | `KaTex:\langle \rangle` | `\langle` `\rangle` | `KaTex:⟮ ⟯` | `⟮ ⟯` | `KaTex:\lgroup \rgroup` | `\lgroup` `\rgroup` | `KaTex:\Uparrow` | `\Uparrow` |
| `KaTeX:∣` | `\|` | `KaTex:\vert` | `\vert` | `KaTex:┌ ┐` | `┌ ┐` | `KaTex:\ulcorner \urcorner` | `\ulcorner` `\urcorner` | `KaTex:\Downarrow` | `\Downarrow` |
| `KaTeX:\|` _(MD语法冲突)_ | `\\|` | `KaTex:\Vert` | `\Vert` | `KaTex:└ ┘` | `└ ┘` | `KaTex:\llcorner \lrcorner` | `\llcorner` `\lrcorner` | `KaTex:\Updownarrow` | `\Updownarrow` |
| `KaTeX:∣ ∣` | `\lvert` `\rvert` | `KaTex:\lVert \rVert` | `\lVert` `\rVert` |  | `\left.` |  | `\right.` | `KaTex:\backslash` | `\backslash` |
| `KaTeX:\lang` `KaTeX:\rang` | `\lang` `\rang` | `KaTeX:\lt \gt` | `\lt \gt` | `KaTex:⟦ ⟧` | `⟦ ⟧` | `KaTex:\llbracket \rrbracket` | `\llbracket` `\rrbracket` | `KaTex:\lBrace \rBrace` | `\lBrace \rBrace` |

可以使用一对表达式 `\left` `KaTeX:s_1` 和 `\right` `KaTeX:s_2` 来将分隔符 `KaTeX:s_1` 和 `KaTeX:s_2` 的高度与其内容的高度进行匹配，例如:

| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTeX:\left\|` | `KaTeX:expr` | `KaTeX:\right\|` |  | `KaTeX:\left\{` | `KaTeX:expr` | `KaTeX:\right\}` |  | `KaTeX:\left\Vert` | `KaTeX:expr` | `KaTeX:\right.` |

### 可变大小的符号

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTeX:\sum` | `\sum` | `KaTeX:\int` | `\int` | `KaTeX:\biguplus` | `\biguplus` | `KaTeX:\bigoplus` | `\bigoplus` | `KaTeX:\bigvee` | `\bigvee` |
| `KaTeX:\prod` | `\prod` | `KaTeX:\oint` | `\oint` | `KaTeX:\bigcap` | `\bigcap` | `KaTeX:\bigotimes` | `\bigotimes` | `KaTeX:\bigwedge` | `\bigwedge` |
| `KaTeX:\coprod` | `\coprod` | `KaTeX:\iint` | `\iint` | `KaTeX:\bigcup` | `\bigcup` | `KaTeX:\bigodot` | `\bigodot` | `KaTeX:\bigodot` | `\bigodot` |

### 标准函数名称

| 预览 | 方法 | 预览 | 方法 | 预览 | 方法 | 预览 | 方法 |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTeX:\arccos` | `\arccos` | `KaTeX:\arcsin` | `\arcsin` | `KaTeX:\arcsin` | `\arcsin` | `KaTeX:\arg` | `\arg` |
| `KaTeX:\cos` | `\cos` | `KaTeX:\cosh` | `\cosh` | `KaTeX:\cot` | `\cot` | `KaTeX:\coth` | `\coth` |
| `KaTeX:\csc` | `\csc` | `KaTeX:\deg` | `\deg` | `KaTeX:\det` | `\det` | `KaTeX:\dim` | `\dim` |
| `KaTeX:\exp` | `\exp` | `KaTeX:\gcd` | `\gcd` | `KaTeX:\hom` | `\hom` | `KaTeX:\inf` | `\inf` |
| `KaTeX:\ker` | `\ker` | `KaTeX:\lg` | `\lg` | `KaTeX:\lim` | `\lim` | `KaTeX:\liminf` | `\liminf` |
| `KaTeX:\limsup` | `\limsup` | `KaTeX:\ln` | `\ln` | `KaTeX:\log` | `\log` | `KaTeX:\max` | `\max` |
| `KaTeX:\min` | `\min` | `KaTeX:\Pr` | `\Pr` | `KaTeX:\sec` | `\sec` | `KaTeX:\sin` | `\sin` |
| `KaTeX:\sinh` | `\sinh` | `KaTeX:\sup` | `\sup` | `KaTeX:\tan` | `\tan` | `KaTeX:\tanh` | `\tanh` |

函数名应该用罗马字体，而不是斜体，例如:

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| Correct: | `\tan(at-n\pi)` | `KaTeX:\rightarrow` | `KaTeX:\tan(at-n\pi)` |
| Incorrect: | `tan(at-n\pi)` | `katex:\rightarrow` | `KaTeX:tan(at-n\pi)` |

### 逻辑与集合论

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTeX:\forall` | `\forall` | `KaTeX:\complement` | `\complement` | `KaTeX:\therefore` | `\therefore` | `KaTeX:\emptyset` | `\emptyset` |
| `KaTeX:\exists` | `\exists` | `KaTeX:\subset` | `\subset` | `KaTeX:\because` | `\because` | `KaTeX:\empty` | `\empty` |
| `KaTeX:\exist` | `\exist` | `KaTeX:\supset` | `\supset` | `KaTeX:\mapsto` | `\mapsto` | `KaTeX:\varnothing` | `\varnothing` |
| `KaTeX:\nexists` | `\nexists` | `KaTeX:\mid` | `\mid` | `KaTeX:\to` | `\to` | `KaTeX:\implies` | `\implies` |
| `KaTeX:\in` | `\in` | `KaTeX:\land` | `\land` | `KaTeX:\gets` | `\gets` | `KaTeX:\impliedby` | `\impliedby` |
| `KaTeX:\isin` | `\isin` | `KaTeX:\lor` | `\lor` | `KaTeX:\leftrightarrow` | `\leftrightarrow` | `KaTeX:\iff` | `\iff` |
| `KaTeX:\notin` | `\notin` | `KaTeX:\ni` | `\ni` | `KaTeX:\notni` | `\notni` | `KaTeX:\neg` `KaTeX:\lnot` | `\neg` 或 `\lnot` |

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTeX:\Set{ x \| x<\frac 1 2 }` | \Set{ x \| x<\frac 1 2 } | `KaTeX:\set{x\|x<5}` | \set{x\|x<5} |

### 宏指令

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTeX:\def\foo{x^2} \foo + \foo` | \def\foo{x^2} \foo + \foo | `KaTeX:\gdef\bar#1{#1^2} \bar{y} + \bar{y}` | \gdef\bar#1{#1^2} \bar{y} + \bar{y} |

### 特殊符号

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTeX:\bra{\phi}` | \bra{\phi} | `KaTeX:\ket{\psi}` | \ket{\psi} | `KaTeX:\braket{\phi\|\psi}` | `\braket{\phi\|\psi}` |
| `KaTeX:\Bra{\phi}` | \Bra{\phi} | `KaTeX:\Ket{\psi}` | \Ket{\psi} | `KaTeX:\Braket{ ϕ \| \frac{∂^2}{∂ t^2} \| ψ }` | `\Braket{ ϕ \| \frac{∂^2}{∂ t^2} \| ψ }` |

## 运算符

### 数学运算符

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\arcsin` | `\arcsin` | `KaTex:\cosec` | `\cosec` | `KaTex:\deg` | `\deg` | `KaTex:\sec` | `\sec` |
| `KaTex:\arccos` | `\arccos` | `KaTex:\cosh` | `\cosh` | `KaTex:\dim` | `\dim` | `KaTex:\sin` | `\sin` |
| `KaTex:\arctan` | `\arctan` | `KaTex:\cot` | `\cot` | `KaTex:\exp` | `\exp` | `KaTex:\sinh` | `\sinh` |
| `KaTex:\arctg` | `\arctg` | `KaTex:\cotg` | `\cotg` | `KaTex:\hom` | `\hom` | `KaTex:\sh` | `\sh` |
| `KaTex:\arcctg` | `\arcctg` | `KaTex:\coth` | `\coth` | `KaTex:\ker` | `\ker` | `KaTex:\tan` | `\tan` |
| `KaTex:\arg` | `\arg` | `KaTex:\csc` | `\csc` | `KaTex:\lg` | `\lg` | `KaTex:\tanh` | `\tanh` |
| `KaTex:\ch` | `\ch` | `KaTex:\ctg` | `\ctg` | `KaTex:\ln` | `\ln` | `KaTex:\tg` | `\tg` |
| `KaTex:\cos` | `\cos` | `KaTex:\cth` | `\cth` | `KaTex:\log` | `\log` | `KaTex:\th` | `\th` |
| `KaTex:\operatorname{f}` | `\operatorname{f}` |
| `KaTex:\argmax` | `\argmax` | `KaTex:\injlim` | `\injlim` | `KaTex:\min` | `\min` | `KaTex:\varinjlim` | `\varinjlim` |
| `KaTex:\argmin` | `\argmin` | `KaTex:\lim` | `\lim` | `KaTex:\plim` | `\plim` | `KaTex:\varliminf` | `\varliminf` |
| `KaTex:\det` | `\det` | `KaTex:\liminf` | `\liminf` | `KaTex:\Pr` | `\Pr` | `KaTex:\varlimsup` | `\varlimsup` |
| `KaTex:\gcd` | `\gcd` | `KaTex:\limsup` | `\limsup` | `KaTex:\projlim` | `\projlim` | `KaTex:\varprojlim` | `\varprojlim` |
| `KaTex:\inf` | `\inf` | `KaTex:\max` | `\max` | `KaTex:\sup` | `\sup` | `KaTex:\operatorname*{f}` | `\operatorname*{f}` |
| `KaTex:\operatornamewithlimits{f}` | `\operatornamewithlimits{f}` |

### 大运算符

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\sum` | `\sum` | `KaTex:\prod` | `\prod` | `KaTex:\bigotimes` | `\bigotimes` | `KaTex:\bigvee` | `\bigvee` |
| `KaTex:\int` | `\int` | `KaTex:\coprod` | `\coprod` | `KaTex:\bigoplus` | `\bigoplus` | `KaTex:\bigwedge` | `\bigwedge` |
| `KaTex:\iint` | `\iint` | `KaTex:\intop` | `\intop` | `KaTex:\bigodot` | `\bigodot` | `KaTex:\bigcap` | `\bigcap` |
| `KaTex:\iiint` | `\iiint` | `KaTex:\smallint` | `\smallint` | `KaTex:\biguplus` | `\biguplus` | `KaTex:\bigcup` | `\bigcup` |
| `KaTex:\oint` | `\oint` | `KaTex:\oiint` | `\oiint` | `KaTex:\oiiint` | `\oiiint` | `KaTex:\bigsqcup` | `\bigsqcup` |

### 分数和二项式

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTex:\frac{a}{b}` | `\frac{a}{b}` | `KaTex:\tfrac{a}{b}` | `\tfrac{a}{b}` |
| `KaTex:{a \over b}` | `{a \over b}` | `KaTex:\dfrac{a}{b}` | `\dfrac{a}{b}` |
| `KaTex:\genfrac ( ] {2pt}{1}a{a+1}` | `\genfrac ( ] {2pt}{1}a{a+1}` | `KaTex:{a \above{2pt} b+1}` | `{a \above{2pt} b+1}` |
| `KaTex:a/b` | `a/b` | `KaTex:\cfrac{a}{1 + \cfrac{1}{b}}` | `\cfrac{a}{1 + \cfrac{1}{b}}` |

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTex:\binom{n}{k}` | `\binom{n}{k}` | `KaTex:\dbinom{n}{k}` | `\dbinom{n}{k}` |
| `KaTex:{n\brace k}` | `{n\brace k}` | `KaTex:{n \choose k}` | `{n \choose k}` |
| `KaTex:\tbinom{n}{k}` | `\tbinom{n}{k}` | `KaTex:{n\brack k}` | `{n\brack k}` |

### \sqrt

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTex:\sqrt{x}` | `\sqrt{x}` | `KaTex:\sqrt[3]{x}` | `\sqrt[3]{x}` |

### 二元运算符

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:+` | `+` | `KaTex:\cdot` | `\cdot` | `KaTex:\gtrdot` | `\gtrdot` | `KaTex:x \pmod a` | `x \pmod a` |
| `KaTex:-` | `-` | `KaTex:\cdotp` | `\cdotp` | `KaTex:\intercal` | `\intercal` | `KaTex:x \pod a` | `x \pod a` |
| `KaTex:/` | `/` | `KaTex:\centerdot` | `\centerdot` | `KaTex:\land` | `\land` | `KaTex:\rhd` | `\rhd` |
| `KaTex:*` | `*` | `KaTex:\circ` | `\circ` | `KaTex:\leftthreetimes` | `\leftthreetimes` | `KaTex:\rightthreetimes` | `\rightthreetimes` |
| `KaTex:\amalg` | `\amalg` | `KaTex:\circledast` | `\circledast` | `KaTex:\ldotp` | `\ldotp` | `KaTex:\rtimes` | `\rtimes` |
| `KaTex:\And` | `\And` | `KaTex:\circledcirc` | `\circledcirc` | `KaTex:\lor` | `\lor` | `KaTex:\setminus` | `\setminus` |
| `KaTex:\ast` | `\ast` | `KaTex:\circleddash` | `\circleddash` | `KaTex:\lessdot` | `\lessdot` | `KaTex:\smallsetminus` | `\smallsetminus` |
| `KaTex:\barwedge` | `\barwedge` | `KaTex:\Cup` | `\Cup` | `KaTex:\lhd` | `\lhd` | `KaTex:\sqcap` | `\sqcap` |
| `KaTex:\bigcirc` | `\bigcirc` | `KaTex:\cup` | `\cup` | `KaTex:\ltimes` | `\ltimes` | `KaTex:\sqcup` | `\sqcup` |
| `KaTex:\bmod` | `\bmod` | `KaTex:\curlyvee` | `\curlyvee` | `KaTex:x\mod a` | `x\mod a` | `KaTex:\times` | `\times` |
| `KaTex:\boxdot` | `\boxdot` | `KaTex:\curlywedge` | `\curlywedge` | `KaTex:\mp` | `\mp` | `KaTex:\unlhd` | `\unlhd` |
| `KaTex:\boxminus` | `\boxminus` | `KaTex:\div` | `\div` | `KaTex:\odot` | `\odot` | `KaTex:\unrhd` | `\unrhd` |
| `KaTex:\boxplus` | `\boxplus` | `KaTex:\divideontimes` | `\divideontimes` | `KaTex:\ominus` | `\ominus` | `KaTex:\uplus` | `\uplus` |
| `KaTex:\boxtimes` | `\boxtimes` | `KaTex:\dotplus` | `\dotplus` | `KaTex:\oplus` | `\oplus` | `KaTex:\vee` | `\vee` |
| `KaTex:\bullet` | `\bullet` | `KaTex:\doublebarwedge` | `\doublebarwedge` | `KaTex:\otimes` | `\otimes` | `KaTex:\veebar` | `\veebar` |
| `KaTex:\Cap` | `\Cap` | `KaTex:\doublecap` | `\doublecap` | `KaTex:\oslash` | `\oslash` | `KaTex:\wedge` | `\wedge` |
| `KaTex:\cap` | `\cap` | `KaTex:\doublecup` | `\doublecup` | `KaTex:\pm` | `\pm` | `KaTex:\plusmn` | `\plusmn` |
| `KaTex:\wr` | `\wr`` |

## 关系

### 关系

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:=` | `=` | `KaTex:\doteqdot` | `\doteqdot` | `KaTex:\lessapprox` | `\lessapprox` | `KaTex:\smile` | `\smile` |
| `KaTex:<` | `<` | `KaTex:\eqcirc` | `\eqcirc` | `KaTex:\lesseqgtr` | `\lesseqgtr` | `KaTex:\sqsubset` | `\sqsubset` |
| `KaTex:>` | `>` | `KaTex:\eqcolon` | `\eqcolon` 或 `\minuscolon` | `KaTex:\lesseqqgtr` | `\lesseqqgtr` | `KaTex:\sqsubseteq` | `\sqsubseteq` |
| `KaTex::` | `:` | `KaTex:\Eqcolon` | `\Eqcolon` 或 `\minuscoloncolon` | `KaTex:\lessgtr` | `\lessgtr` | `KaTex:\sqsupset` | `\sqsupset` |
| `KaTex:\approx` | `\approx` | `KaTex:\eqqcolon` | `\eqqcolon` 或 `\equalscolon` | `KaTex:\lesssim` | `\lesssim` | `KaTex:\sqsupseteq` | `\sqsupseteq` |
| `KaTex:\approxcolon` | `\approxcolon` | `KaTex:\Eqqcolon` | `\Eqqcolon` 或 `\equalscoloncolon` | `KaTex:\ll` | `\ll` | `KaTex:\Subset` | `\Subset` |
| `KaTex:\approxcoloncolon` | `\approxcoloncolon` | `KaTex:\eqsim` | `\eqsim` | `KaTex:\lll` | `\lll` | `KaTex:\subset` | `\subset` 或 `\sub` |
| `KaTex:\approxeq` | `\approxeq` | `KaTex:\eqslantgtr` | `\eqslantgtr` | `KaTex:\llless` | `\llless` | `KaTex:\subseteq` | `\subseteq` 或 `\sube` |
| `KaTex:\asymp` | `\asymp` | `KaTex:\eqslantless` | `\eqslantless` | `KaTex:\lt` | `\lt` | `KaTex:\subseteqq` | `\subseteqq` |
| `KaTex:\backepsilon` | `\backepsilon` | `KaTex:\equiv` | `\equiv` | `KaTex:\mid` | `\mid` | `KaTex:\succ` | `\succ` |
| `KaTex:\backsim` | `\backsim` | `KaTex:\fallingdotseq` | `\fallingdotseq` | `KaTex:\models` | `\models` | `KaTex:\succapprox` | `\succapprox` |
| `KaTex:\backsimeq` | `\backsimeq` | `KaTex:\frown` | `\frown` | `KaTex:\multimap` | `\multimap` | `KaTex:\succcurlyeq` | `\succcurlyeq` |
| `KaTex:\between` | `\between` | `KaTex:\ge` | `\ge` | `KaTex:\origof` | `\origof` | `KaTex:\succeq` | `\succeq` |
| `KaTex:\bowtie` | `\bowtie` | `KaTex:\geq` | `\geq` | `KaTex:\owns` | `\owns` | `KaTex:\succsim` | `\succsim` |
| `KaTex:\bumpeq` | `\bumpeq` | `KaTex:\geqq` | `\geqq` | `KaTex:\parallel` | `\parallel` | `KaTex:\Supset` | `\Supset` |
| `KaTex:\Bumpeq` | `\Bumpeq` | `KaTex:\geqslant` | `\geqslant` | `KaTex:\perp` | `\perp` | `KaTex:\supset` | `\supset` |
| `KaTex:\circeq` | `\circeq` | `KaTex:\gg` | `\gg` | `KaTex:\pitchfork` | `\pitchfork` | `KaTex:\supseteq` | `\supseteq` 或 `\supe` |
| `KaTex:\colonapprox` | `\colonapprox` | `KaTex:\ggg` | `\ggg` | `KaTex:\prec` | `\prec` | `KaTex:\supseteqq` | `\supseteqq` |
| `KaTex:\Colonapprox` | `\Colonapprox` 或 `\coloncolonapprox` | `KaTex:\gggtr` | `\gggtr` | `KaTex:\precapprox` | `\precapprox` | `KaTex:\thickapprox` | `\thickapprox` |
| `KaTex:\coloneq` | `\coloneq` 或 `\colonminus` | `KaTex:\gt` | `\gt` | `KaTex:\preccurlyeq` | `\preccurlyeq` | `KaTex:\thicksim` | `\thicksim` |
| `KaTex:\Coloneq` | `\Coloneq` 或 `\coloncolonminus` | `KaTex:\gtrapprox` | `\gtrapprox` | `KaTex:\preceq` | `\preceq` | `KaTex:\trianglelefteq` | `\trianglelefteq` |
| `KaTex:\coloneqq` | `\coloneqq` 或 `\colonequals` | `KaTex:\gtreqless` | `\gtreqless` | `KaTex:\precsim` | `\precsim` | `KaTex:\triangleq` | `\triangleq` |
| `KaTex:\Coloneqq` | `\Coloneqq` 或 `\coloncolonequals` | `KaTex:\gtreqqless` | `\gtreqqless` | `KaTex:\propto` | `\propto` | `KaTex:\trianglerighteq` | `\trianglerighteq` |
| `KaTex:\colonsim` | `\colonsim` | `KaTex:\gtrless` | `\gtrless` | `KaTex:\risingdotseq` | `\risingdotseq` | `KaTex:\varpropto` | `\varpropto` |
| `KaTex:\Colonsim` | `\Colonsim` 或 `\coloncolonsim` | `KaTex:\gtrsim` | `\gtrsim` | `KaTex:\shortmid` | `\shortmid` | `KaTex:\vartriangle` | `\vartriangle` |
| `KaTex:\cong` | `\cong` | `KaTex:\imageof` | `\imageof` | `KaTex:\shortparallel` | `\shortparallel` | `KaTex:\vartriangleleft` | `\vartriangleleft` |
| `KaTex:\curlyeqprec` | `\curlyeqprec` | `KaTex:\in` | `\in` 或 `\isin` | `KaTex:\sim` | `\sim` | `KaTex:\vartriangleright` | `\vartriangleright` |
| `KaTex:\curlyeqsucc` | `\curlyeqsucc` | `KaTex:\Join` | `\Join` | `KaTex:\simcolon` | `\simcolon` | `KaTex:\vcentcolon` | `\vcentcolon` 或 `\ratio` |
| `KaTex:\dashv` | `\dashv` | `KaTex:\le` | `\le` | `KaTex:\simcoloncolon` | `\simcoloncolon` | `KaTex:\vdash` | `\vdash` |
| `KaTex:\dblcolon` | `\dblcolon` 或 `\coloncolon` | `KaTex:\leq` | `\leq` | `KaTex:\simeq` | `\simeq` | `KaTex:\vDash` | `\vDash` |
| `KaTex:\doteq` | `\doteq` | `KaTex:\leqq` | `\leqq` | `KaTex:\smallfrown` | `\smallfrown` | `KaTex:\Vdash` | `\Vdash` |
| `KaTex:\Doteq` | `\Doteq` | `KaTex:\leqslant` | `\leqslant` | `KaTex:\smallsmile` | `\smallsmile` | `KaTex:\Vvdash` | `\Vvdash` |

### 否定关系

| :- | :- | :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- | :- | :- |
| `KaTex:\gnapprox` | `\gnapprox` | `KaTex:\ngeqslant` | `\ngeqslant` | `KaTex:\nsubseteq` | `\nsubseteq` | `KaTex:\precneqq` | `\precneqq` |
| `KaTex:\gneq` | `\gneq` | `KaTex:\ngtr` | `\ngtr` | `KaTex:\nsubseteqq` | `\nsubseteqq` | `KaTex:\precnsim` | `\precnsim` |
| `KaTex:\gneqq` | `\gneqq` | `KaTex:\nleq` | `\nleq` | `KaTex:\nsucc` | `\nsucc` | `KaTex:\subsetneq` | `\subsetneq` |
| `KaTex:\gnsim` | `\gnsim` | `KaTex:\nleqq` | `\nleqq` | `KaTex:\nsucceq` | `\nsucceq` | `KaTex:\subsetneqq` | `\subsetneqq` |
| `KaTex:\gvertneqq` | `\gvertneqq` | `KaTex:\nleqslant` | `\nleqslant` | `KaTex:\nsupseteq` | `\nsupseteq` | `KaTex:\succnapprox` | `\succnapprox` |
| `KaTex:\lnapprox` | `\lnapprox` | `KaTex:\nless` | `\nless` | `KaTex:\nsupseteqq` | `\nsupseteqq` | `KaTex:\succneqq` | `\succneqq` |
| `KaTex:\lneq` | `\lneq` | `KaTex:\nmid` | `\nmid` | `KaTex:\ntriangleleft` | `\ntriangleleft` | `KaTex:\succnsim` | `\succnsim` |
| `KaTex:\lneqq` | `\lneqq` | `KaTex:\notin` | `\notin` | `KaTex:\ntrianglelefteq` | `\ntrianglelefteq` | `KaTex:\supsetneq` | `\supsetneq` |
| `KaTex:\lnsim` | `\lnsim` | `KaTex:\notni` | `\notni` | `KaTex:\ntriangleright` | `\ntriangleright` | `KaTex:\supsetneqq` | `\supsetneqq` |
| `KaTex:\lvertneqq` | `\lvertneqq` | `KaTex:\nparallel` | `\nparallel` | `KaTex:\ntrianglerighteq` | `\ntrianglerighteq` | `KaTex:\varsubsetneq` | `\varsubsetneq` |
| `KaTex:\ncong` | `\ncong` | `KaTex:\nprec` | `\nprec` | `KaTex:\nvdash` | `\nvdash` | `KaTex:\varsubsetneqq` | `\varsubsetneqq` |
| `KaTex:\ne` | `\ne` | `KaTex:\npreceq` | `\npreceq` | `KaTex:\nvDash` | `\nvDash` | `KaTex:\varsupsetneq` | `\varsupsetneq` |
| `KaTex:\neq` | `\neq` | `KaTex:\nshortmid` | `\nshortmid` | `KaTex:\nVDash` | `\nVDash` | `KaTex:\varsupsetneqq` | `\varsupsetneqq` |
| `KaTex:\ngeq` | `\ngeq` | `KaTex:\nshortparallel` | `\nshortparallel` | `KaTex:\nVdash` | `\nVdash` |
| `KaTex:\ngeqq` | `\ngeqq` | `KaTex:\nsim` | `\nsim` | `KaTex:\precnapprox` | `\precnapprox` |

`KaTex:\not =` `\not =`

### 箭头

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTex:\circlearrowleft` | `\circlearrowleft` | `KaTex:\leftharpoonup` | `\leftharpoonup` | `KaTex:\rArr` | `\rArr` |
| `KaTex:\circlearrowright` | `\circlearrowright` | `KaTex:\leftleftarrows` | `\leftleftarrows` | `KaTex:\rarr` | `\rarr` |
| `KaTex:\curvearrowleft` | `\curvearrowleft` | `KaTex:\leftrightarrow` | `\leftrightarrow` | `KaTex:\restriction` | `\restriction` |
| `KaTex:\curvearrowright` | `\curvearrowright` | `KaTex:\Leftrightarrow` | `\Leftrightarrow` | `KaTex:\rightarrow` | `\rightarrow` |
| `KaTex:\Darr` | `\Darr` | `KaTex:\leftrightarrows` | `\leftrightarrows` | `KaTex:\Rightarrow` | `\Rightarrow` |
| `KaTex:\dArr` | `\dArr` | `KaTex:\leftrightharpoons` | `\leftrightharpoons` | `KaTex:\rightarrowtail` | `\rightarrowtail` |
| `KaTex:\darr` | `\darr` | `KaTex:\leftrightsquigarrow` | `\leftrightsquigarrow` | `KaTex:\rightharpoondown` | `\rightharpoondown` |
| `KaTex:\dashleftarrow` | `\dashleftarrow` | `KaTex:\Lleftarrow` | `\Lleftarrow` | `KaTex:\rightharpoonup` | `\rightharpoonup` |
| `KaTex:\dashrightarrow` | `\dashrightarrow` | `KaTex:\longleftarrow` | `\longleftarrow` | `KaTex:\rightleftarrows` | `\rightleftarrows` |
| `KaTex:\downarrow` | `\downarrow` | `KaTex:\Longleftarrow` | `\Longleftarrow` | `KaTex:\rightleftharpoons` | `\rightleftharpoons` |
| `KaTex:\Downarrow` | `\Downarrow` | `KaTex:\longleftrightarrow` | `\longleftrightarrow` | `KaTex:\rightrightarrows` | `\rightrightarrows` |
| `KaTex:\downdownarrows` | `\downdownarrows` | `KaTex:\Longleftrightarrow` | `\Longleftrightarrow` | `KaTex:\rightsquigarrow` | `\rightsquigarrow` |
| `KaTex:\downharpoonleft` | `\downharpoonleft` | `KaTex:\longmapsto` | `\longmapsto` | `KaTex:\Rrightarrow` | `\Rrightarrow` |
| `KaTex:\downharpoonright` | `\downharpoonright` | `KaTex:\longrightarrow` | `\longrightarrow` | `KaTex:\Rsh` | `\Rsh` |
| `KaTex:\gets` | `\gets` | `KaTex:\Longrightarrow` | `\Longrightarrow` | `KaTex:\searrow` | `\searrow` |
| `KaTex:\Harr` | `\Harr` | `KaTex:\looparrowleft` | `\looparrowleft` | `KaTex:\swarrow` | `\swarrow` |
| `KaTex:\hArr` | `\hArr` | `KaTex:\looparrowright` | `\looparrowright` | `KaTex:\to` | `\to` |
| `KaTex:\harr` | `\harr` | `KaTex:\Lrarr` | `\Lrarr` | `KaTex:\twoheadleftarrow` | `\twoheadleftarrow` |
| `KaTex:\hookleftarrow` | `\hookleftarrow` | `KaTex:\lrArr` | `\lrArr` | `KaTex:\twoheadrightarrow` | `\twoheadrightarrow` |
| `KaTex:\hookrightarrow` | `\hookrightarrow` | `KaTex:\lrarr` | `\lrarr` | `KaTex:\Uarr` | `\Uarr` |
| `KaTex:\iff` | `\iff` | `KaTex:\Lsh` | `\Lsh` | `KaTex:\uArr` | `\uArr` |
| `KaTex:\impliedby` | `\impliedby` | `KaTex:\mapsto` | `\mapsto` | `KaTex:\uarr` | `\uarr` |
| `KaTex:\implies` | `\implies` | `KaTex:\nearrow` | `\nearrow` | `KaTex:\uparrow` | `\uparrow` |
| `KaTex:\Larr` | `\Larr` | `KaTex:\nleftarrow` | `\nleftarrow` | `KaTex:\Uparrow` | `\Uparrow` |
| `KaTex:\lArr` | `\lArr` | `KaTex:\nLeftarrow` | `\nLeftarrow` | `KaTex:\updownarrow` | `\updownarrow` |
| `KaTex:\larr` | `\larr` | `KaTex:\nleftrightarrow` | `\nleftrightarrow` | `KaTex:\Updownarrow` | `\Updownarrow` |
| `KaTex:\leadsto` | `\leadsto` | `KaTex:\nLeftrightarrow` | `\nLeftrightarrow` | `KaTex:\upharpoonleft` | `\upharpoonleft` |
| `KaTex:\leftarrow` | `\leftarrow` | `KaTex:\nrightarrow` | `\nrightarrow` | `KaTex:\upharpoonright` | `\upharpoonright` |
| `KaTex:\Leftarrow` | `\Leftarrow` | `KaTex:\nRightarrow` | `\nRightarrow` | `KaTex:\upuparrows` | `\upuparrows` |
| `KaTex:\leftarrowtail` | `\leftarrowtail` | `KaTex:\nwarrow` | `\nwarrow` |
| `KaTex:\leftharpoondown` | `\leftharpoondown` | `KaTex:\Rarr` | `\Rarr` |

### 可扩展箭头

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTex:\xleftarrow{abc}` | `\xleftarrow{abc}` | `KaTex:\xrightarrow[under]{over}` | `\xrightarrow[under]{over}` |
| `KaTex:\xLeftarrow{abc}` | `\xLeftarrow{abc}` | `KaTex:\xRightarrow{abc}` | `\xRightarrow{abc}` |
| `KaTex:\xleftrightarrow{abc}` | `\xleftrightarrow{abc}` | `KaTex:\xLeftrightarrow{abc}` | `\xLeftrightarrow{abc}` |
| `KaTex:\xhookleftarrow{abc}` | `\xhookleftarrow{abc}` | `KaTex:\xhookrightarrow{abc}` | `\xhookrightarrow{abc}` |
| `KaTex:\xtwoheadleftarrow{abc}` | `\xtwoheadleftarrow{abc}` | `KaTex:\xtwoheadrightarrow{abc}` | `\xtwoheadrightarrow{abc}` |
| `KaTex:\xleftharpoonup{abc}` | `\xleftharpoonup{abc}` | `KaTex:\xrightharpoonup{abc}` | `\xrightharpoonup{abc}` |
| `KaTex:\xleftharpoondown{abc}` | `\xleftharpoondown{abc}` | `KaTex:\xrightharpoondown{abc}` | `\xrightharpoondown{abc}` |
| `KaTex:\xleftrightharpoons{abc}` | `\xleftrightharpoons{abc}` | `KaTex:\xrightleftharpoons{abc}` | `\xrightleftharpoons{abc}` |
| `KaTex:\xtofrom{abc}` | `\xtofrom{abc}` | `KaTex:\xmapsto{abc}` | `\xmapsto{abc}` |
| `KaTex:\xlongequal{abc}` | `\xlongequal{abc}` |

## 符号和标点符号

### 符号和标点符号

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTex:% comment` | `% comment` | `KaTex:\dots` | `\dots` | `KaTex:\KaTeX` | `\KaTeX` |
| `KaTex:\%` | `\%` | `KaTex:\cdots` | `\cdots` | `KaTex:\LaTeX` | `\LaTeX` |
| `KaTex:\#` | `\#` | `KaTex:\ddots` | `\ddots` | `KaTex:\TeX` | `\TeX` |
| `KaTex:\&` | `\&` | `KaTex:\ldots` | `\ldots` | `KaTex:\nabla` | `\nabla` |
| `KaTex:\_` | `\_` | `KaTex:\vdots` | `\vdots` | `KaTex:\infty` | `\infty` |
| `KaTex:\text{\textunderscore}` | `\text{\textunderscore}` | `KaTex:\dotsb` | `\dotsb` | `KaTex:\infin` | `\infin` |
| `KaTex:\text{--}` | `\text{--}` | `KaTex:\dotsc` | `\dotsc` | `KaTex:\checkmark` | `\checkmark` |
| `KaTex:\text{\textendash}` | `\text{\textendash}` | `KaTex:\dotsi` | `\dotsi` | `KaTex:\dag` | `\dag` |
| `KaTex:\text{---}` | `\text{---}` | `KaTex:\dotsm` | `\dotsm` | `KaTex:\dagger` | `\dagger` |
| `KaTex:\text{\textemdash}` | `\text{\textemdash}` | `KaTex:\dotso` | `\dotso` | `KaTex:\text{\textdagger}` | `\text{\textdagger}` |
| `KaTex:\text{\textasciitilde}` | `\text{\textasciitilde}` | `KaTex:\sdot` | `\sdot` | `KaTex:\ddag` | `\ddag` |
| `KaTex:\text{\textasciicircum}` | `\text{\textasciicircum}` | `KaTex:\mathellipsis` | `\mathellipsis` | `KaTex:\ddagger` | `\ddagger` |
| `` KaTex:` `` | \` | `KaTex:\text{\textellipsis}` | `\text{\textellipsis}` | `KaTex:\text{\textdaggerdbl}` | `\text{\textdaggerdbl}` |
| `KaTex:\text{\textquoteleft}` | `text{\textquoteleft}` | `KaTex:\Box` | `\Box` | `KaTex:\Dagger` | `\Dagger` |
| `KaTex:\lq` | `\lq` | `KaTex:\square` | `\square` | `KaTex:\angle` | `\angle` |
| `KaTex:\text{\textquoteright}` | `\text{\textquoteright}` | `KaTex:\blacksquare` | `\blacksquare` | `KaTex:\measuredangle` | `\measuredangle` |
| `KaTex:\rq` | `\rq` | `KaTex:\triangle` | `\triangle` | `KaTex:\sphericalangle` | `\sphericalangle` |
| `KaTex:\text{\textquotedblleft}` | `\text{\textquotedblleft}` | `KaTex:\triangledown` | `\triangledown` | `KaTex:\top` | `\top` |
| `KaTex:"` | `"` | `KaTex:\triangleleft` | `\triangleleft` | `KaTex:\bot` | `\bot` |
| `KaTex:\text{\textquotedblright}` | `\text{\textquotedblright}` | `KaTex:\triangleright` | `\triangleright` | `KaTex:\$` | `\$` |
| `KaTex:\colon` | `\colon` | `KaTex:\bigtriangledown` | `\bigtriangledown` | `KaTex:\text{\textdollar}` | `\text{\textdollar}` |
| `KaTex:\backprime` | `\backprime` | `KaTex:\bigtriangleup` | `\bigtriangleup` | `KaTex:\pounds` | `\pounds` |
| `KaTex:\prime` | `\prime` | `KaTex:\blacktriangle` | `\blacktriangle` | `KaTex:\mathsterling` | `\mathsterling` |
| `KaTex:\text{\textless}` | `\text{\textless}` | `KaTex:\blacktriangledown` | `\blacktriangledown` | `KaTex:\text{\textsterling}` | `\text{\textsterling}` |
| `KaTex:\text{\textgreater}` | `\text{\textgreater}` | `KaTex:\blacktriangleleft` | `\blacktriangleleft` | `KaTex:\yen` | `\yen` |
| `KaTex:\text{\textbar}` | `\text{\textbar}` | `KaTex:\blacktriangleright` | `\blacktriangleright` | `KaTex:\surd` | `\surd` |
| `KaTex:\text{\textbardbl}` | `\text{\textbardbl}` | `KaTex:\diamond` | `\diamond` | `KaTex:\degree` | `\degree` |
| `KaTex:\text{\textbraceleft}` | `\text{\textbraceleft}` | `KaTex:\Diamond` | `\Diamond` | `KaTex:\text{\textdegree}` | `\text{\textdegree}` |
| `KaTex:\text{\textbraceright}` | `\text{\textbraceright}` | `KaTex:\lozenge` | `\lozenge` | `KaTex:\mho` | `\mho` |
| `KaTex:\text{\textbackslash}` | `\text{\textbackslash}` | `KaTex:\blacklozenge` | `\blacklozenge` | `KaTex:\diagdown` | `\diagdown` |
| `KaTex:\text{\P}` | `\text{\P}` 或 `\P` | `KaTex:\star` | `\star` | `KaTex:\diagup` | `\diagup` |
| `KaTex:\text{\S}` | `\text{\S}` 或 `\S` | `KaTex:\bigstar` | `\bigstar` | `KaTex:\flat` | `\flat` |
| `KaTex:\text{\sect}` | `\text{\sect}` | `KaTex:\clubsuit` | `\clubsuit` | `KaTex:\natural` | `\natural` |
| `KaTex:\copyright` | `\copyright` | `KaTex:\clubs` | `\clubs` | `KaTex:\sharp` | `\sharp` |
| `KaTex:\circledR` | `\circledR` | `KaTex:\diamondsuit` | `\diamondsuit` | `KaTex:\heartsuit` | `\heartsuit` |
| `KaTex:\text{\textregistered}` | `\text{\textregistered}` | `KaTex:\diamonds` | `\diamonds` | `KaTex:\hearts` | `\hearts` |
| `KaTex:\circledS` | `\circledS` | `KaTex:\spadesuit` | `\spadesuit` | `KaTex:\spades` | `\spades` |
| `KaTex:\text{\textcircled a}` | `\text{\textcircled a}` | `KaTex:\maltese` | `\maltese` | `KaTex:\minuso` | `\minuso` |

## 环境

### 环境 1

```KaTeX
\begin{matrix}
   a & b \\
   c & d
\end{matrix}
```

```LaTeX
\begin{matrix}
   a & b \\
   c & d
\end{matrix}
```

### 环境 2

```KaTeX
\begin{array}{cc}
   a & b \\
   c & d
\end{array}
```

```LaTeX
\begin{array}{cc}
   a & b \\
   c & d
\end{array}
```

### 环境 3

```KaTeX
\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
```

```LaTeX
\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
```

### 环境 4

```KaTeX
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix}
```

```LaTeX
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix}
```

### 环境 5

```KaTeX
\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}
```

```LaTeX
\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}
```

### 环境 6

```KaTeX
\begin{Vmatrix}
   a & b \\
   c & d
\end{Vmatrix}
```

```LaTeX
\begin{Vmatrix}
   a & b \\
   c & d
\end{Vmatrix}
```

### 环境 7

```KaTeX
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
```

```LaTeX
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
```

### 环境 8

```KaTeX
\def\arraystretch{1.5}
   \begin{array}{c:c:c}
   a & b & c \\ \hline
   d & e & f \\
   \hdashline
   g & h & i
\end{array}
```

```LaTeX
\def\arraystretch{1.5}
   \begin{array}{c:c:c}
   a & b & c \\ \hline
   d & e & f \\
   \hdashline
   g & h & i
\end{array}
```

### 环境 9

```KaTeX
x = \begin{cases}
   a &\text{if } b \\
   c &\text{if } d
\end{cases}
```

```LaTeX
x = \begin{cases}
   a &\text{if } b \\
   c &\text{if } d
\end{cases}
```

### 环境 10

```KaTeX
\begin{rcases}
   a &\text{if } b \\
   c &\text{if } d
\end{rcases}⇒…
```

```LaTeX
\begin{rcases}
   a &\text{if } b \\
   c &\text{if } d
\end{rcases}⇒…
```

### 环境 11

```KaTeX
\begin{smallmatrix}
   a & b \\
   c & d
\end{smallmatrix}
```

```LaTeX
\begin{smallmatrix}
   a & b \\
   c & d
\end{smallmatrix}
```

### 环境 12

```KaTeX
\sum_{
\begin{subarray}{l}
   i\in\Lambda\\
   0<j<n
\end{subarray}}
```

```LaTeX
\sum_{
\begin{subarray}{l}
   i\in\Lambda\\
   0<j<n
\end{subarray}}
```

### 环境 13

```KaTeX
\begin{equation}
\begin{split}  a &=b+c\\
      &=e+f
\end{split}
\end{equation}
```

```LaTeX
\begin{equation}
\begin{split}  a &=b+c\\
      &=e+f
\end{split}
\end{equation}
```

### 环境 14

```KaTeX
\begin{align}
   a&=b+c \\
   d+e&=f
\end{align}
```

```LaTeX
\begin{align}
   a&=b+c \\
   d+e&=f
\end{align}
```

### 环境 15

```KaTeX
\begin{gather}
   a=b \\
   e=b+c
\end{gather}
```

```LaTeX
\begin{gather}
   a=b \\
   e=b+c
\end{gather}
```

### 环境 16

```KaTeX
\begin{alignat}{2}
   10&x+&3&y=2\\
   3&x+&13&y=4
\end{alignat}
```

```LaTeX
\begin{alignat}{2}
   10&x+&3&y=2\\
   3&x+&13&y=4
\end{alignat}
```

### 环境 17

```KaTeX
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
```

```LaTeX
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
```

## 样式、颜色、大小和字体

### Color 颜色

| :- | :- |
| :- | :- |
| `KaTex:\color{blue} F=ma` | `\color{blue} F=ma` |
| `KaTex:\textcolor{blue}{F=ma}` | `\textcolor{blue}{F=ma}` |
| `KaTex:\textcolor{#228B22}{F=ma}` | `\textcolor{#228B22}{F=ma}` |
| `KaTex:\colorbox{aqua}{$F=ma$}` | `\colorbox{aqua}{$F=ma$}` |
| `KaTex:\fcolorbox{red}{aqua}{$F=ma$}` | `\fcolorbox{red}{aqua}{$F=ma$}` |

### 字体

| :- | :- | :- | :- | :- | :- |
| :- | :- | :- | :- | :- | :- |
| `KaTex:\Huge AB` | `\Huge AB` | `KaTex:\normalsize AB` | `\normalsize AB` | `KaTex:\normalsize AB` | \normalsize AB |
| `KaTex:\huge AB` | `\huge AB` | `KaTex:\huge AB` | `\huge AB` | `KaTex:\small AB` | \small AB |
| `KaTex:\LARGE AB` | `\LARGE AB` | `KaTex:\LARGE AB` | `\LARGE AB` | `KaTex:\footnotesize AB` | \footnotesize AB |
| `KaTex:\Large AB` | `\Large AB` | `KaTex:\Large AB` | `\Large AB` | `KaTex:\scriptsize AB` | \scriptsize AB |
| `KaTex:\large AB` | `\large AB` | `KaTex:\large AB` | `\large AB` | `KaTex:\tiny AB` | \tiny AB |

### 样式

| :- | :- | :- | :- |
| :- | :- | :- | :- |
| `KaTex:\displaystyle\sum_{i=1}^n` | \displaystyle\sum_{i=1}^n | `KaTex:\textstyle\sum_{i=1}^n` | \textstyle\sum_{i=1}^n |
| `KaTex:\scriptstyle x` | \scriptstyle x | `KaTex:\scriptscriptstyle x` | \scriptscriptstyle x |
| `KaTex:\lim\limits_x` | \lim\limits_x | `KaTex:\lim\nolimits_x` | \lim\nolimits_x |
| `KaTex:\verb!x^2!` | \verb!x^2! |

## 另见

- [LaTeX 官网](https://www.latex-project.org/) _(latex-project.org)_
- [KaTeX 官网](https://katex.org/) _(katex.org)_
- [symbols.pdf](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf) _(cmor-faculty.rice.edu)_

来源：[https://github.com/jaywcjlove/reference/blob/main/docs/latex.md](https://github.com/jaywcjlove/reference/blob/main/docs/latex.md)

获取日期：2026-10-15
