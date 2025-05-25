class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }
        const sorted__s = s.split('').sort().join('');
        const sorted__t = t.split('').sort().join('');

        return sorted__s === sorted__t;
    }
}
