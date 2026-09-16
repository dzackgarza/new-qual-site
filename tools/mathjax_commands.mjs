// Write tools/qualc/mathjax_commands.json: every TeX command the site's MathJax defines.
//
// The site loads MathJax 3's `tex-chtml-full` component, which registers the
// `require` package and `AllPackages`. A command is defined when one of those
// packages' parse maps (macros, delimiters, characters) names it, or when the
// text-mode maps `textmacros` uses inside `\text{}` do. The set is read from
// MathJax's own maps rather than listed by hand.
//
//   just mathjax-commands
import {writeFileSync} from 'node:fs';
import {AllPackages} from 'mathjax-full@3.2.2/js/input/tex/AllPackages.js';
import 'mathjax-full@3.2.2/js/input/tex/require/RequireConfiguration.js';
import {ConfigurationHandler} from 'mathjax-full@3.2.2/js/input/tex/Configuration.js';
import {MapHandler} from 'mathjax-full@3.2.2/js/input/tex/MapHandler.js';
import {TextBaseConfiguration} from 'mathjax-full@3.2.2/js/input/tex/textmacros/TextMacrosConfiguration.js';

const names = new Set();
function collect(configuration) {
  for (const kind of ['macro', 'delimiter', 'character']) {
    for (const mapName of configuration.handler[kind] || []) {
      const map = MapHandler.getMap(mapName);
      if (!map) throw new Error(`MathJax names a parse map it does not register: ${mapName}`);
      // Regular-expression maps (letters, digits) name no command.
      if (!map.map) continue;
      for (const key of map.map.keys()) {
        const name = key.replace(/^\\/, '');
        if (/^[A-Za-z]+$/.test(name)) names.add(name);
      }
    }
  }
}
for (const pkg of ['require', ...AllPackages]) {
  const configuration = ConfigurationHandler.get(pkg);
  if (!configuration) throw new Error(`MathJax has no configuration for package ${pkg}`);
  collect(configuration);
}
collect(TextBaseConfiguration);

const target = new URL('./qualc/mathjax_commands.json', import.meta.url);
writeFileSync(target, JSON.stringify([...names].sort(), null, 0).replace(/","/g, '",\n"').replace(/^\[/, '[\n').replace(/\]$/, '\n]\n'));
