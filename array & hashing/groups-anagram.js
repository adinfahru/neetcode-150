class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupsMap = {};

        for (const kata of strs){
            const keys = kata.split('').sort().join('');

            if (!groupsMap[keys]){
                groupsMap[keys] = [kata];

            } else {
                groupsMap[keys].push(kata);
            }
        }

        return Object.values(groupsMap)
    }
}
