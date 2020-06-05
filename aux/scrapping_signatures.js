//
// Open
// https://wiki2.org/en/List_of_file_signatures
// Run this script in browser console
//
const aFinal = [];
document.querySelectorAll("table.wikitable tr").forEach((tr, trIdx) => {
  if (trIdx === 0) {
    return;
  }
  const aTd = tr.querySelectorAll("td");
  const aSign = aTd[0].querySelectorAll('pre');
  aSign.forEach((pre, preIdx) => {
    const oLine = {
      signature: null,
      extension: null,
      offset: null,
      description: null,
    };
    let sign = pre.textContent.trim().replace(/\n/ig, ' ');
    let offset = null;
    let ext = null;
    let desc = null;
    if (sign) {
      oLine.signature = sign;
      oLine.variable = false;
      if (sign.indexOf('??') > 0) {
        oLine.variable = true;
      }
      offset = parseInt(aTd[2].textContent.trim(), 10);
      if (!isNaN(offset)) {
        oLine.offset = offset;
      }
      ext = aTd[3].innerHTML.trim().split('<br>').map(e => {
        e=e.replace(/\n/, ' ').replace(/<[^>]+>/ig, ' ').trim(); return e !== '' ? e : null
      }).filter(e => e);
      if (ext.length > 0) {
        let extStr = ext;
        if (ext.length === 1) {
          extStr = ext.join('').replace(/\n/ig, ' ').replace(/[\ ]+/ig, ' ');
          ext = extStr.split(' ').map(e => e.trim());
        }
        // Thor hammer for 53 5A 44 44 88 F0 27 33
        if (ext.indexOf('setup.ex_)') > -1) {
          ext = ['ex_']
        }
        oLine.extension = [].concat(ext);
        
      }
      desc = aTd[4].textContent.trim();
      oLine.description = desc.replace(/\n/ig, ' ').replace(/<[^>]+>/ig, ' ').replace(/\[\d+\]/ig, ' ').trim();
    }
    aFinal.push(oLine);
  });
});
// console.log(JSON.stringify(aFinal));
copy(JSON.stringify(aFinal));
console.log('Done: Fix the following');
