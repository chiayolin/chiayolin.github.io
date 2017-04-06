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

var commit_url = "https://github.com/chiayolin/chiayolin.github.io/commit/"

function getLatestSHA(url, callback) {
	$.ajax({ dataType: 'json', url: url }).done((data) => callback(data));
}

$(document).ready(() => {
	getLatestSHA("https://api.github.com/repositories/18872887/commits",
		(data) => {
			var sha = data[0].sha
			$("#git-commit-sha").attr('href', commit_url + sha);
			$("#git-commit-sha").text(sha.slice(0, 13)) 
		})
});