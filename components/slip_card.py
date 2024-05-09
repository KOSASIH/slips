# components/slip_card.py
import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, Grid, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/styles';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  card: {
    maxWidth: 345,
    margin: theme.spacing(2),
  },
  media: {
    height: 140,
  },
}));

interface SlipCardProps {
  slip: {
    id: number;
    title: string;
    description: string;
    created_at: string;
  };
  onDelete: (id: number) => void;
}

const SlipCard: React.FC<SlipCardProps> = ({ slip, onDelete }) => {
  const classes = useStyles();
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const handleMouseEnter = () => setIsHovered(true);
    const handleMouseLeave = () => setIsHovered(false);

    document.addEventListener('mouseenter', handleMouseEnter);
    document.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      document.removeEventListener('mouseenter', handleMouseEnter);
      document.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, []);

  return (
    <Card className={classes.card} elevation={isHovered? 10 : 2}>
      <CardContent>
        <Typography variant="h5" component="h2">
          {slip.title}
        </Typography>
        <Typography variant="body2" color="textSecondary">
          {slip.description}
        </Typography>
        <Typography variant="caption" display="block">
          Created at: {slip.created_at}
        </Typography>
      </CardContent>
      <Grid container justify="flex-end">
        <Button
          variant="contained"
          color="primary"
          component={Link}
          to={`/slips/${slip.id}/edit`}
        >
          Edit
        </Button>
        <Button
          variant="contained"
          color="secondary"
          onClick={() => onDelete(slip.id)}
        >
          Delete
        </Button>
      </Grid>
    </Card>
  );
};

export default SlipCard;
