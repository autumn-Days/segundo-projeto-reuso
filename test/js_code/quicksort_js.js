function quicksort(arr, left, right) {
    if (left < right) {
        let pivot = arr[Math.floor((left + right) / 2)];
        let i = left;
        let j = right;

        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;

            if (i <= j) {
                let temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }

        if (left < j) quicksort(arr, left, j);
        if (i < right) quicksort(arr, i, right);
    }
}

function main() {
    let v = [34,7,23,32,5,62,78,1,45,9,12,56,89,4,27,16,3,90,11,54,21,8,67,14,29,6,10,2,99,41,18,25,30,15,55,19,28,13,20,17];

    quicksort(v, 0, v.length - 1);

    console.log(v.join(" "));
}

main();
