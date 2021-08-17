class Point{
    constructor(row, column){
        this.row = row;
        this.column = column;
    }
}

class NodeInfo{
    constructor(g,h,point, previous){
        this.f = g + h;
        this.g = g;
        this.h = h;
        this.point = point;
        this.previous = previous;
    }
}


export default class AStar{

    constructor(){
        this.water = [2717,2715, 2833, 2773, 2775, 2834, 2832, 2716, 2714,2776,2777,2836,2835]; //tileset
    }

    getPath(startRow, startCol, endRow, endCol, level){

        let iterations = 0;
        let start = new NodeInfo(0, 500, new Point(startRow, startCol), null);
        let goal = new NodeInfo(0, 0, new Point(endRow, endCol), null);
        let open = [start]
        let closed = []
        while( open.length > 0 ){
            iterations++;
            let smallest = this.getSmallestNode(open);
            if ( smallest.point.row == goal.point.row && smallest.point.column == goal.point.column )
            {
                goal.previous = smallest;
                let path = ["STOP"]
                while ( goal.previous != null ){
               
                    path.push([goal.point.row,goal.point.column])

                    goal = goal.previous;
                    if( goal == null)
                        break;
                }

                return path;

            }
            else
            {
                this.getSuccesors(open, closed, goal, smallest, level);
                closed.push(smallest)
            }
        }
        return ["NO PATH"];
    }

    getSmallestNode(open){
        let smallest = open[0];
        let index = 0;
        for( let i = 1; i < open.length; i++){
            if( open[i].f < smallest.f){
                smallest = open[i];
                index = i;
            }
        }

        open.splice(index,1);
        return smallest;
    }

    manhattanDistance(nodeA, nodeB){
        let row = Math.abs( nodeA.row - nodeB.row );
        let column = Math.abs( nodeA.column - nodeB.column );
        return row + column;
    }

    getSuccesors(open, closed, goal, smallest, level){
        let up = new Point( smallest.point.row - 1, smallest.point.column );
        let down = new Point( smallest.point.row + 1, smallest.point.column );
        let left = new Point( smallest.point.row, smallest.point.column - 1);
        let right = new Point( smallest.point.row , smallest.point.column + 1 );

        let options = [up,down,left,right]

        for(let i = 0; i < 4;i++){
            
            let option = options[i];
            let validRow = (0 <= option.row) && (option.row < level.length);
            let validColumn = (0 <= option.column) && (option.column < level[0].length);
            if( validRow && validColumn && !this.water.includes(level[option.row][option.column]) )
            {

                let inOpen = this.pointInList(open, option);
                let inClosed = this.pointInList(closed, option);

                let costSoFar = smallest.g + 1;

                if( inOpen != null){
                    continue;
                }
                else if ( inClosed != null){
                   
                    if( inClosed.g + 2 < inClosed.g)
                    {
                        closed.slice(closed.indexOf(inClosed),1);
                        let distance = this.manhattanDistance(inClosed.point, goal.point);
                        open.push(inClosed);

                    }
                }
                else if(inClosed == null && inOpen == null)
                {

                    let distance = this.manhattanDistance(option, goal.point);
                    let node = new NodeInfo(smallest.g + 1, distance, option, smallest)
                    open.push(node);

                }
            }
        };
    }

    pointInList(pointList, move){
        for( let i = 0; i < pointList.length; i++){
            let p = pointList[i];
            if( p.point.row == move.row && p.point.column == move.column){
                return p;
            }
        }
        return null;
    }
}
