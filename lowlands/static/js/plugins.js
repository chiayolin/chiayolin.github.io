/* 
 * Gerneral Plugins - plugins.js 
 * Copyright (C) 2017  Chiayo Lin <chiayo.lin@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 */

/* latest commit URL from Github */
var COMMIT_URL = "https://github.com/chiayolin/chiayolin.github.io/commit/"

function getLatestSHA(url, callback) {
  $.ajax({ dataType: 'json', url: url }).done((data) => callback(data));
}

/* main */
$(document).ready(() => {

  /* display latest SHA */
  getLatestSHA("https://api.github.com/repositories/18872887/commits",
    (data) => {
      var sha = data[0].sha
      $("#git-commit-sha").attr('href', COMMIT_URL + sha);
      $("#git-commit-sha").text(sha.slice(0, 13)) 
    });
  
  /* baffle.js */
  window.baffle('#brand-name').start().set({ speed: 50 }).reveal(1500, 1500);
  setTimeout(() => $('.site-title-cursor').show(), 3000);

});
