import java.util.Arrays;

/**
 * Created by wangwenjie on 2017/2/23.
 *
 */
public class QuickSort {
    public static void quickSort(int[] arr){
        qsort(arr, 0, arr.length-1);
    }
    private static void qsort(int[] arr, int low, int high){
        if (low < high){
            int location = partition(arr, low, high);//将数组分为两部分
            qsort(arr, low, location - 1);//递归排序左子数组
            qsort(arr, location + 1, high);//递归排序右子数组
        }
    }
    private static int partition(int[] arr, int low, int high){
        int location = (low + high) / 2;
        int pivot = arr[location];//枢轴记录
        while (low < high) {
            while (low < high && arr[high] >= pivot) {
                --high;
            }
            arr[low] = arr[high];//交换比枢轴小的记录到左端
            while (low < high && arr[low] <= pivot) {
                ++low;
            }
            arr[high] = arr[low];//交换比枢轴小的记录到右端
        }
        //扫描完成，枢轴到位
        arr[low] = pivot;
        //返回的是枢轴的位置
        return low;
    }

    public static void main(String[] args) {
        int[] arr = {10,12,3,4,6,1,23,11};
        QuickSort.quickSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
